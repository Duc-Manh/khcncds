package com.khcncds.genco2.controller;

// Thêm các dòng import này
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @org.springframework.beans.factory.annotation.Autowired
    private org.springframework.jdbc.core.JdbcTemplate jdbcTemplate;

    @GetMapping({"/", "/index"})
    public String index(org.springframework.ui.Model model) {
        long formCount = 0;
        long commentCount = 0;
        long approCount = 0;
        long councilCount = 0;

        try {
            Long f = jdbcTemplate.queryForObject("SELECT COUNT(*) FROM form", Long.class);
            if (f != null) formCount = f;
        } catch(Exception e) {}

        try {
            Long c = jdbcTemplate.queryForObject("SELECT COUNT(*) FROM comment", Long.class);
            if (c != null) commentCount = c;
        } catch(Exception e) {}

        try {
            Long a = jdbcTemplate.queryForObject("SELECT COUNT(*) FROM appro", Long.class);
            if (a != null) approCount = a;
        } catch(Exception e) {}

        try {
            Long hd = jdbcTemplate.queryForObject("SELECT COUNT(*) FROM council", Long.class);
            if (hd != null) councilCount = hd;
        } catch(Exception e) {}

        model.addAttribute("formCount", formCount);
        model.addAttribute("commentCount", commentCount);
        model.addAttribute("approCount", approCount);
        model.addAttribute("councilCount", councilCount);

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
    @org.springframework.beans.factory.annotation.Autowired
    private com.khcncds.genco2.repository.ExpertRepository expertRepository;

    @GetMapping("/expert")
    public String expert(@org.springframework.web.bind.annotation.RequestParam(defaultValue = "1") int page,
                         @org.springframework.web.bind.annotation.RequestParam(required = false) String field,
                         org.springframework.ui.Model model) {
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
        return "expert"; 
    }

    @GetMapping("/proposal")
    public String proposal() {
        return "proposal"; 
    }
    @GetMapping("/evaluate")
    public String evaluate() {
        return "evaluate"; 
    }
}