package com.khcncds.genco2.controller;

import com.khcncds.genco2.entity.UserEntity;
import com.khcncds.genco2.repository.UserRepository;
import jakarta.servlet.http.HttpSession;
import com.khcncds.genco2.service.DynamicRegisterService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import com.khcncds.genco2.service.DynamicApproveService;
import com.khcncds.genco2.entity.Expert;
import com.khcncds.genco2.repository.ExpertRepository;

import java.util.List;

@Controller
public class AdminController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private DynamicRegisterService dynamicRegisterService;

    @Autowired
    private DynamicApproveService dynamicApproveService;

    @Autowired
    private ExpertRepository expertRepository;

    @Autowired
    private com.khcncds.genco2.repository.QuestionRepository questionRepository;

    @Autowired
    private com.khcncds.genco2.repository.FormRepository formRepository;

    @Autowired
    private com.khcncds.genco2.repository.CommentRepository commentRepository;

    @GetMapping("/admin")
    public String adminPage(HttpSession session, Model model) {
        // Kiểm tra xem user đã đăng nhập chưa
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            // Nếu chưa đăng nhập, đá về trang login
            return "redirect:/login";
        }

        // Đã đăng nhập -> Đưa thông tin user ra giao diện
        model.addAttribute("user", loggedInUser);
        return "admin";
    }

    @GetMapping("/admin/pro")
    public String adminProPage(@org.springframework.web.bind.annotation.RequestParam(defaultValue = "1") int page, 
                              @org.springframework.web.bind.annotation.RequestParam(required = false) String field,
                              HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);

        // Fetch experts for "Chuyên gia" tab
        int pageSize = 10;
        org.springframework.data.domain.Pageable pageable = org.springframework.data.domain.PageRequest.of(page - 1, pageSize);
        org.springframework.data.domain.Page<com.khcncds.genco2.entity.Expert> expertPage;
        
        if (field != null && !field.isEmpty() && !field.equals("Lĩnh vực chuyên môn")) {
            expertPage = expertRepository.findByField(field, pageable);
            model.addAttribute("selectedField", field);
        } else {
            expertPage = expertRepository.findAll(pageable);
            model.addAttribute("selectedField", "Lĩnh vực chuyên môn");
        }
        
        model.addAttribute("expertPage", expertPage);

        return "admin_pro";
    }

    @GetMapping("/admin/other")
    public String adminOtherPage(HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        return "admin_other";
    }

    @GetMapping("/admin/news")
    public String adminNewsPage(HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        return "admin_news";
    }

    @GetMapping("/admin/notice")
    public String adminNoticePage(HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        return "admin_notice";
    }

    @GetMapping("/admin/employ")
    public String adminEmployPage(HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        
        // Fetch all users to display in the table
        List<UserEntity> users = userRepository.findAll();
        model.addAttribute("users", users);
        
        // Fetch all registers to display in the account registration table
        java.util.List<com.khcncds.genco2.entity.RegisterEntity> registers = dynamicRegisterService.findAllRegistersForCurrentYear();
        model.addAttribute("registers", registers);

        // Fetch approved accounts (appro table)
        java.util.List<com.khcncds.genco2.entity.ApprovedAccountDTO> approAccounts = dynamicApproveService.getApproAccounts();
        model.addAttribute("approAccounts", approAccounts);

        // Fetch council accounts (council table)
        java.util.List<com.khcncds.genco2.entity.ApprovedAccountDTO> councilAccounts = dynamicApproveService.getCouncilAccounts();
        model.addAttribute("councilAccounts", councilAccounts);
        
        // Fetch all experts
        List<Expert> experts = expertRepository.findAll();
        model.addAttribute("experts", experts);
        
        return "admin_employ";
    }

    @PostMapping("/admin/approve")
    public String approveAccount(@RequestParam("registerId") Long registerId, HttpSession session, RedirectAttributes redirectAttributes) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        
        String[] result = dynamicApproveService.approveAccount(registerId);
        redirectAttributes.addFlashAttribute("approvedAccount", result[0]);
        redirectAttributes.addFlashAttribute("approvedAim", result[1]);
        
        return "redirect:/admin/employ";
    }

    @PostMapping("/admin/reject")
    public String rejectAccount(@RequestParam("registerId") Long registerId, HttpSession session, RedirectAttributes redirectAttributes) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        
        dynamicApproveService.rejectAccount(registerId);
        redirectAttributes.addFlashAttribute("rejectedAccount", true);
        
        return "redirect:/admin/employ";
    }

    @PostMapping("/admin/appro/delete")
    public String deleteApproAccount(@RequestParam("username") String username, HttpSession session) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        dynamicApproveService.deleteApproAccount(username);
        return "redirect:/admin/employ";
    }

    @PostMapping("/admin/council/delete")
    public String deleteCouncilAccount(@RequestParam("username") String username, HttpSession session) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        dynamicApproveService.deleteCouncilAccount(username);
        return "redirect:/admin/employ";
    }

    @PostMapping("/admin/expert/delete")
    public String deleteExpertAccount(@RequestParam("username") String username, HttpSession session) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        dynamicApproveService.deleteExpertAccount(username);
        return "redirect:/admin/employ";
    }

    @GetMapping("/admin/idea")
    public String adminIdeaPage(HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        return "admin_idea";
    }

    @GetMapping("/admin/council")
    public String adminCouncilPage(@org.springframework.web.bind.annotation.RequestParam(defaultValue = "1") int page, 
                              @org.springframework.web.bind.annotation.RequestParam(required = false) String field,
                              HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        
        // Fetch council members
        java.util.List<com.khcncds.genco2.entity.ApprovedAccountDTO> councilMembers = dynamicApproveService.getCouncilAccounts();
        model.addAttribute("councilMembers", councilMembers);
        
        // Fetch questions for "Tham vấn" tab
        java.util.List<com.khcncds.genco2.entity.Question> questions = questionRepository.findAll(org.springframework.data.domain.Sort.by(org.springframework.data.domain.Sort.Direction.DESC, "time"));
        model.addAttribute("questions", questions);
        
        // Fetch experts for "Chuyên gia" tab
        int pageSize = 10;
        org.springframework.data.domain.Pageable pageable = org.springframework.data.domain.PageRequest.of(page - 1, pageSize);
        org.springframework.data.domain.Page<com.khcncds.genco2.entity.Expert> expertPage;
        
        if (field != null && !field.isEmpty() && !field.equals("Lĩnh vực chuyên môn")) {
            expertPage = expertRepository.findByField(field, pageable);
            model.addAttribute("selectedField", field);
        } else {
            expertPage = expertRepository.findAll(pageable);
            model.addAttribute("selectedField", "Lĩnh vực chuyên môn");
        }
        
        model.addAttribute("expertPage", expertPage);
        
        long pendingFormsCount = formRepository.countByState(1);
        model.addAttribute("pendingFormsCount", pendingFormsCount);
        
        java.util.List<com.khcncds.genco2.entity.Form> pendingFormsList = formRepository.findByState(1);
        model.addAttribute("pendingFormsList", pendingFormsList);
        
        java.util.List<com.khcncds.genco2.entity.Comment> myComments = commentRepository.findByFullNameOrderByTimeDesc(loggedInUser.getFullName());
        model.addAttribute("myComments", myComments);
        
        return "admin_council";
    }

    @GetMapping("/admin/regis")
    public String adminRegisPage(HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        return "admin_regis";
    }
    @PostMapping("/admin/user/create")
    public String createUser(
            @RequestParam("department") String department,
            @RequestParam("position") String position,
            @RequestParam("fullName") String fullName,
            @RequestParam("username") String username,
            @RequestParam("password") String password,
            @RequestParam("email") String email,
            @RequestParam("phone") String phone,
            HttpSession session) {
        
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        
        UserEntity newUser = new UserEntity();
        newUser.setDepartment(department);
        newUser.setPosition(position);
        newUser.setFullName(fullName);
        newUser.setUsername(username);
        newUser.setPassword(password); // In a real app, hash this!
        newUser.setEmail(email);
        newUser.setPhone(phone);
        newUser.setRole("admin"); // Default as requested
        
        userRepository.save(newUser);
        
        return "redirect:/admin/employ";
    }
}
