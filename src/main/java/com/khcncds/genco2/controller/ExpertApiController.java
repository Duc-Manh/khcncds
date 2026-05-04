package com.khcncds.genco2.controller;

import com.khcncds.genco2.entity.Expert;
import com.khcncds.genco2.repository.ExpertRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/expert")
public class ExpertApiController {

    @Autowired
    private ExpertRepository expertRepository;

    @PostMapping("/register")
    public ResponseEntity<?> registerExpert(@RequestBody Expert expert) {
        try {
            // Check mandatory fields
            if (expert.getFullName() == null || expert.getFullName().trim().isEmpty() ||
                expert.getCccd() == null || expert.getCccd().trim().isEmpty() ||
                expert.getEmail() == null || expert.getEmail().trim().isEmpty() ||
                expert.getPhone() == null || expert.getPhone().trim().isEmpty() ||
                expert.getDepartment() == null || expert.getDepartment().trim().isEmpty() ||
                expert.getMajor() == null || expert.getMajor().trim().isEmpty() ||
                expert.getTrend() == null || expert.getTrend().trim().isEmpty() ||
                expert.getGoogle() == null || expert.getGoogle().trim().isEmpty()) {
                
                Map<String, String> error = new HashMap<>();
                error.put("message", "Bạn cần nhập đủ thông tin cần thiết");
                return ResponseEntity.badRequest().body(error);
            }

            expertRepository.save(expert);
            
            Map<String, String> response = new HashMap<>();
            response.put("message", "Đăng ký thành công!");
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            Map<String, String> error = new HashMap<>();
            error.put("message", "Đã xảy ra lỗi hệ thống: " + e.getMessage());
            return ResponseEntity.internalServerError().body(error);
        }
    }
}
