package com.khcncds.genco2.controller;

// Thêm các dòng import này
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/index")
    public String index() {
        // Trả về file index.html nằm trong thư mục src/main/resources/templates
        return "index"; 
    }
    @GetMapping("/login")
    public String login() {
        // Trả về file login.html trong thư mục templates
        return "login"; 
    }
    @GetMapping("/news")
    public String news() {
        // Trả về file news.html trong thư mục templates
        return "news"; 
    }
    @GetMapping("/notice")
    public String notice() {
        // Trả về file notice.html trong thư mục templates
        return "notice"; 
    }
    @GetMapping("/internal")
    public String internal() {
        // Trả về file internal.html trong thư mục templates
        return "internal"; 
    }
    @GetMapping("/expert")
    public String expert() {
        // Trả về file expert.html trong thư mục templates
        return "expert"; 
    }
    @GetMapping("/expert-regis")
    public String expertRegis() {
        // Trả về file expert-regis.html trong thư mục templates
        return "expert-regis"; 
    }
}