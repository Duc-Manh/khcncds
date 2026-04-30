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

@Controller
public class LoginController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private DynamicRegisterService dynamicRegisterService;

    @Autowired
    private DynamicApproveService dynamicApproveService;

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

        // 3. Nếu không có trong users, kiểm tra trong bảng appro của năm hiện tại
        if (dynamicApproveService.validateApproUser(username, password)) {
            session.setAttribute("APPRO_USER", username);
            return "redirect:/regis_idea";
        }

        // 4. Nếu không có trong appro, kiểm tra trong bảng council của năm hiện tại
        if (dynamicApproveService.validateCouncilUser(username, password)) {
            session.setAttribute("COUNCIL_USER", username);
            return "redirect:/council";
        }

        // 5. Tài khoản hoặc mật khẩu không hợp lệ
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
    public String regisIdeaPage(HttpSession session) {
        if (session.getAttribute("APPRO_USER") == null) {
            return "redirect:/login";
        }
        return "regis_idea";
    }

    @GetMapping("/council")
    public String councilPage(HttpSession session) {
        if (session.getAttribute("COUNCIL_USER") == null) {
            return "redirect:/login";
        }
        return "council";
    }
}