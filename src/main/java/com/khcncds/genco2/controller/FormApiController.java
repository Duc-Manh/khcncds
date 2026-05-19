package com.khcncds.genco2.controller;

import com.khcncds.genco2.entity.Form;
import com.khcncds.genco2.repository.FormRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpSession;
import com.khcncds.genco2.service.DynamicApproveService;

import java.time.LocalDateTime;

@RestController
@RequestMapping("/api/forms")
public class FormApiController {

    @Autowired
    private FormRepository formRepository;
    
    @Autowired
    private DynamicApproveService dynamicApproveService;

    @PostMapping("/submit")
    public ResponseEntity<?> submitForm(@RequestBody Form form, HttpSession session) {
        try {
            // Lấy thông tin user đăng nhập
            String username = (String) session.getAttribute("APPRO_USER");
            if (username != null) {
                java.util.Map<String, Object> userDetails = dynamicApproveService.getUserDetails(username, "ge2.");
                if (!userDetails.isEmpty()) {
                    form.setDepartment((String) userDetails.get("department"));
                    form.setPosition((String) userDetails.get("position"));
                    form.setFullName((String) userDetails.get("full_name"));
                    form.setEmail((String) userDetails.get("email"));
                    form.setPhone((String) userDetails.get("phone"));
                }
            }

            form.setTime(LocalDateTime.now());
            form.setState(1); // Mặc định state = 1 theo yêu cầu
            formRepository.save(form);
            return ResponseEntity.ok().body("{\"message\": \"Bạn đã gửi thành công\"}");
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError().body("{\"message\": \"Có lỗi xảy ra: " + e.getMessage() + "\"}");
        }
    }

    @GetMapping("/latest")
    public ResponseEntity<?> getLatestForm() {
        try {
            Form form = formRepository.findFirstByOrderByIdDesc();
            if (form != null) {
                return ResponseEntity.ok(form);
            }
            return ResponseEntity.notFound().build();
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError().body("{\"message\": \"Có lỗi xảy ra: " + e.getMessage() + "\"}");
        }
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getFormById(@PathVariable Long id) {
        try {
            java.util.Optional<Form> formOpt = formRepository.findById(id);
            if (formOpt.isPresent()) {
                return ResponseEntity.ok(formOpt.get());
            }
            return ResponseEntity.notFound().build();
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError().body("{\"message\": \"Có lỗi xảy ra: " + e.getMessage() + "\"}");
        }
    }
}
