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

import java.util.List;

@Controller
public class AdminController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private DynamicRegisterService dynamicRegisterService;

    @Autowired
    private DynamicApproveService dynamicApproveService;

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

    @GetMapping("/admin/idea")
    public String adminIdeaPage(HttpSession session, Model model) {
        UserEntity loggedInUser = (UserEntity) session.getAttribute("LOGGED_IN_USER");
        if (loggedInUser == null) {
            return "redirect:/login";
        }
        model.addAttribute("user", loggedInUser);
        return "admin_idea";
    }
}
