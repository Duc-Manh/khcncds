package com.khcncds.genco2.controller;

import com.khcncds.genco2.entity.UserEntity;
import com.khcncds.genco2.repository.UserRepository;
import com.khcncds.genco2.service.DynamicRegisterService;
import com.khcncds.genco2.service.DynamicApproveService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import java.util.Optional;
import com.khcncds.genco2.entity.Expert;
import com.khcncds.genco2.repository.ExpertRepository;
import com.khcncds.genco2.repository.QuestionRepository;

@Controller
public class LoginController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private DynamicRegisterService dynamicRegisterService;

    @Autowired
    private DynamicApproveService dynamicApproveService;

    @Autowired
    private ExpertRepository expertRepository;

    @Autowired
    private QuestionRepository questionRepository;

    @Autowired
    private com.khcncds.genco2.repository.FormRepository formRepository;

    @Autowired
    private com.khcncds.genco2.service.MailService mailService;

    @Autowired
    private com.khcncds.genco2.repository.CommentRepository commentRepository;

    @PostMapping("/login")
    public String handleLogin(
            @RequestParam("username") String username,
            @RequestParam("password") String password,
            @RequestParam("captcha") String captcha,
            HttpSession session,
            Model model
    ) {
        // 1. Kiểm tra Captcha
        String sessionCaptcha = (String) session.getAttribute("CAPTCHA_SESSION_KEY");
        if (sessionCaptcha == null || !sessionCaptcha.equalsIgnoreCase(captcha)) {
            model.addAttribute("error", "Mã xác thực không chính xác!");
            return "login";
        }

        // 2. Tìm User trong Database Admin (bảng users)
        Optional<UserEntity> userOpt = userRepository.findByUsername(username);
        if (userOpt.isPresent()) {
            UserEntity user = userOpt.get();
            if (user.getPassword().equals(password)) {
                session.setAttribute("LOGGED_IN_USER", user);
                return "redirect:/admin";
            }
        }

        // 3. Phân loại kiểm tra dựa trên tiền tố của username
        if (username.startsWith("ge2.hdkh")) {
            if (dynamicApproveService.validateCouncilUser(username, password)) {
                session.setAttribute("COUNCIL_USER", username);
                session.setAttribute("USER_FULLNAME", dynamicApproveService.getFullName(username, "ge2.hdkh"));
                return "redirect:/council";
            }
        } else if (username.startsWith("ge2.")) {
            if (dynamicApproveService.validateApproUser(username, password)) {
                session.setAttribute("APPRO_USER", username);
                session.setAttribute("USER_FULLNAME", dynamicApproveService.getFullName(username, "ge2."));
                return "redirect:/regis_idea";
            }
        } else if (username.startsWith("cg.")) {
            if (dynamicApproveService.validateExpertUser(username, password)) {
                session.setAttribute("EXPERT_USER", username);
                session.setAttribute("USER_FULLNAME", dynamicApproveService.getFullName(username, "cg."));
                return "redirect:/expert-regis";
            }
        }

        // 6. Tài khoản hoặc mật khẩu không hợp lệ
        model.addAttribute("error", "Tài khoản hoặc mật khẩu không chính xác!");
        return "login";
    }

    @PostMapping("/register")
    public String handleRegister(
            @RequestParam("department") String department,
            @RequestParam("position") String position,
            @RequestParam("fullName") String fullName,
            @RequestParam("aim") String aim,
            @RequestParam("email") String email,
            @RequestParam(value = "phone", required = false) String phone
    ) {
        dynamicRegisterService.saveRegister(department, position, fullName, aim, email, phone);

        return "redirect:/login?registered=true";
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/login";
    }

    @GetMapping("/regis_idea")
    public String regisIdeaPage(HttpSession session, Model model) {
        String username = (String) session.getAttribute("APPRO_USER");
        if (username == null) {
            return "redirect:/login";
        }
        
        String fullName = dynamicApproveService.getFullName(username, "ge2.");
        session.setAttribute("USER_FULLNAME", fullName);
        
        model.addAttribute("fullName", fullName);
        return "regis_idea";
    }

    @GetMapping("/council")
    public String councilPage(@org.springframework.web.bind.annotation.RequestParam(defaultValue = "1") int page, 
                              @org.springframework.web.bind.annotation.RequestParam(required = false) String field,
                              HttpSession session, Model model) {
        String username = (String) session.getAttribute("COUNCIL_USER");
        if (username == null) {
            return "redirect:/login";
        }
        
        String fullName = dynamicApproveService.getFullName(username, "ge2.hdkh");
        session.setAttribute("USER_FULLNAME", fullName);
        
        model.addAttribute("fullName", fullName);
        
        java.util.Map<String, Object> councilData = dynamicApproveService.getUserDetails(username, "ge2.hdkh");
        model.addAttribute("council", councilData);
        
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
        
        java.util.List<com.khcncds.genco2.entity.Comment> myComments = commentRepository.findByFullNameOrderByTimeDesc(fullName);
        model.addAttribute("myComments", myComments);
        
        return "council";
    }


    @PostMapping("/submit_question")
    @org.springframework.web.bind.annotation.ResponseBody
    public org.springframework.http.ResponseEntity<?> submitQuestion(
            @org.springframework.web.bind.annotation.RequestBody java.util.Map<String, Object> payload, HttpSession session) {
        String username = (String) session.getAttribute("COUNCIL_USER");
        com.khcncds.genco2.entity.UserEntity adminUser = (com.khcncds.genco2.entity.UserEntity) session.getAttribute("LOGGED_IN_USER");
        
        if (username == null && adminUser == null) {
            return org.springframework.http.ResponseEntity.status(401).body("Unauthorized");
        }
        
        String qFullName = "";
        String qDepartment = "";
        String qPosition = "";
        String qPhone = "";
        String qEmail = "";

        if (username != null) {
            java.util.Map<String, Object> councilData = dynamicApproveService.getUserDetails(username, "ge2.hdkh");
            if (councilData.isEmpty()) {
                return org.springframework.http.ResponseEntity.status(401).body("User not found");
            }
            qFullName = (String) councilData.get("full_name");
            qDepartment = (String) councilData.get("department");
            qPosition = (String) councilData.get("position");
            qPhone = (String) councilData.get("phone");
            qEmail = (String) councilData.get("email");
        } else {
            qFullName = adminUser.getFullName();
            qDepartment = adminUser.getDepartment();
            qPosition = adminUser.getPosition();
            qPhone = adminUser.getPhone();
            qEmail = adminUser.getEmail();
        }

        String fieldSelect = (String) payload.get("fieldSelect");
        String inputTitle = (String) payload.get("title");
        String questionText = (String) payload.get("question");
        java.util.List<Integer> expertIds = (java.util.List<Integer>) payload.get("expertIds");
        
        String combinedTitle = fieldSelect + " - " + inputTitle;

        com.khcncds.genco2.entity.Question q = new com.khcncds.genco2.entity.Question();
        q.setTime(java.time.LocalDateTime.now());
        q.setFullName(qFullName);
        q.setDepartment(qDepartment);
        q.setPosition(qPosition);
        q.setPhone(qPhone);
        q.setEmail(qEmail);
        q.setTitle(combinedTitle);
        q.setQuestion(questionText);
        q.setState("1");
        
        java.util.List<String> ranks = new java.util.ArrayList<>();
        java.util.List<String> fullNames = new java.util.ArrayList<>();
        java.util.List<String> depts = new java.util.ArrayList<>();
        java.util.List<String> positions = new java.util.ArrayList<>();
        java.util.List<String> fields = new java.util.ArrayList<>();
        java.util.List<String> phones = new java.util.ArrayList<>();
        java.util.List<String> emails = new java.util.ArrayList<>();
        
        if (expertIds != null) {
            for (Integer eId : expertIds) {
                com.khcncds.genco2.entity.Expert expert = expertRepository.findById(eId.longValue()).orElse(null);
                if (expert != null) {
                    ranks.add(expert.getRank() != null ? expert.getRank() : "");
                    fullNames.add(expert.getFullName() != null ? expert.getFullName() : "");
                    depts.add(expert.getDepartment() != null ? expert.getDepartment() : "");
                    positions.add(expert.getPosition() != null ? expert.getPosition() : "");
                    fields.add(expert.getField() != null ? expert.getField() : "");
                    phones.add(expert.getPhone() != null ? expert.getPhone() : "");
                    emails.add(expert.getEmail() != null ? expert.getEmail() : "");
                    
                    if (expert.getEmail() != null && !expert.getEmail().trim().isEmpty()) {
                        String expertEmail = expert.getEmail().trim();
                        new Thread(() -> {
                            mailService.sendConsultationEmail(expertEmail);
                        }).start();
                    }
                }
            }
        }
        
        q.setCgRank(String.join(", ", ranks));
        q.setCgFullName(String.join(", ", fullNames));
        q.setCgDepartment(String.join(", ", depts));
        q.setCgPosition(String.join(", ", positions));
        q.setCgField(String.join(", ", fields));
        q.setCgPhone(String.join(", ", phones));
        q.setCgEmail(String.join(", ", emails));
        q.setCgAnswer(""); 
        
        questionRepository.save(q);
        
        return org.springframework.http.ResponseEntity.ok("Success");
    }

    @GetMapping("/expert-regis")
    public String expertRegisPage(HttpSession session, Model model) {
        String username = (String) session.getAttribute("EXPERT_USER");
        if (username == null) {
            return "redirect:/login";
        }
        
        Optional<Expert> expertOpt = expertRepository.findFirstByUsername(username);
        if (expertOpt.isPresent()) {
            Expert expert = expertOpt.get();
            session.setAttribute("USER_FULLNAME", expert.getFullName());
            model.addAttribute("fullName", expert.getFullName());
            model.addAttribute("expert", expert);
        } else {
            String fullName = dynamicApproveService.getFullName(username, "cg.");
            session.setAttribute("USER_FULLNAME", fullName);
            model.addAttribute("fullName", fullName);
        }
        
        // Fetch questions for "Tham vấn" tab
        java.util.List<com.khcncds.genco2.entity.Question> questions = questionRepository.findAll(org.springframework.data.domain.Sort.by(org.springframework.data.domain.Sort.Direction.DESC, "time"));
        model.addAttribute("questions", questions);
        
        return "expert-regis";
    }

    @PostMapping("/expert/answer/save")
    public String saveExpertAnswer(@RequestParam("questionId") Long questionId,
                                   @RequestParam("answer") String answer,
                                   HttpSession session,
                                   org.springframework.web.servlet.mvc.support.RedirectAttributes redirectAttributes) {
        String username = (String) session.getAttribute("EXPERT_USER");
        if (username == null) {
            return "redirect:/login";
        }
        String fullName = (String) session.getAttribute("USER_FULLNAME");

        Optional<com.khcncds.genco2.entity.Question> qOpt = questionRepository.findById(questionId);
        if (qOpt.isPresent()) {
            com.khcncds.genco2.entity.Question q = qOpt.get();
            if (q.getCgFullName() != null && fullName != null) {
                String[] names = q.getCgFullName().split(",");
                int index = -1;
                for (int i = 0; i < names.length; i++) {
                    if (names[i].trim().equals(fullName.trim())) {
                        index = i;
                        break;
                    }
                }
                
                if (index != -1) {
                    String[] answers = new String[names.length];
                    if (q.getCgAnswer() != null) {
                        String[] currentAnswers = q.getCgAnswer().split(",", -1);
                        for (int i = 0; i < Math.min(currentAnswers.length, answers.length); i++) {
                            answers[i] = currentAnswers[i];
                        }
                    }
                    for (int i = 0; i < answers.length; i++) {
                        if (answers[i] == null) answers[i] = "";
                    }
                    
                    String safeAnswer = answer != null ? answer.replace(",", "，") : "";
                    answers[index] = safeAnswer.trim();
                    
                    q.setCgAnswer(String.join(",", answers));
                    questionRepository.save(q);
                    redirectAttributes.addFlashAttribute("success", "Lưu câu trả lời thành công!");
                }
            }
        }
        return "redirect:/expert-regis";
    }

    @PostMapping("/expert-regis/save")
    public String saveExpertRegistration(
            @RequestParam("cccd") String cccd,
            @RequestParam(value = "rank", required = false) String rank,
            @RequestParam(value = "field", required = false) String field,
            @RequestParam(value = "major", required = false) String major,
            @RequestParam("trend") String trend,
            @RequestParam(value = "orcid", required = false) String orcid,
            @RequestParam(value = "gate", required = false) String gate,
            HttpSession session
    ) {
        String username = (String) session.getAttribute("EXPERT_USER");
        if (username == null) {
            return "redirect:/login";
        }
        
        Optional<Expert> expertOpt = expertRepository.findFirstByUsername(username);
        if (expertOpt.isPresent()) {
            Expert expert = expertOpt.get();
            expert.setCccd(cccd);
            
            if (rank != null && !rank.equals("Chọn")) {
                expert.setRank(rank);
            }
            if (field != null && !field.equals("Chọn lĩnh vực")) {
                expert.setField(field);
            }
            if (major != null) {
                expert.setMajor(major);
            }
            expert.setTrend(trend);
            if (orcid != null) {
                expert.setOrcid(orcid);
            }
            if (gate != null) {
                expert.setGate(gate);
            }
            
            expert.setAccept(2);
            
            expertRepository.save(expert);
        }
        
        return "redirect:/expert-regis?success=true";
    }
}