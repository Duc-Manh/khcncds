package com.khcncds.genco2.controller;

import com.khcncds.genco2.entity.Comment;
import com.khcncds.genco2.repository.CommentRepository;
import com.khcncds.genco2.service.DynamicApproveService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpSession;

import java.time.LocalDateTime;

@RestController
@RequestMapping("/api/comments")
public class CommentApiController {

    @Autowired
    private CommentRepository commentRepository;

    @Autowired
    private DynamicApproveService dynamicApproveService;

    @PostMapping("/submit")
    public ResponseEntity<?> submitComment(@RequestBody Comment comment, HttpSession session) {
        try {
            // Lấy thông tin user đăng nhập
            String username = (String) session.getAttribute("COUNCIL_USER");
            com.khcncds.genco2.entity.UserEntity adminUser = (com.khcncds.genco2.entity.UserEntity) session.getAttribute("LOGGED_IN_USER");
            if (username != null) {
                java.util.Map<String, Object> userDetails = dynamicApproveService.getUserDetails(username, "ge2.hdkh");
                if (!userDetails.isEmpty()) {
                    comment.setDepartment((String) userDetails.get("department"));
                    comment.setPosition((String) userDetails.get("position"));
                    comment.setFullName((String) userDetails.get("full_name"));
                    comment.setEmail((String) userDetails.get("email"));
                    comment.setPhone((String) userDetails.get("phone"));
                }
            } else if (adminUser != null) {
                comment.setDepartment(adminUser.getDepartment());
                comment.setPosition(adminUser.getPosition());
                comment.setFullName(adminUser.getFullName());
                comment.setEmail(adminUser.getEmail());
                comment.setPhone(adminUser.getPhone());
            }

            comment.setTime(LocalDateTime.now());
            comment.setState(1); // Mặc định state = 1 theo yêu cầu
            commentRepository.save(comment);
            return ResponseEntity.ok().body("{\"message\": \"Bạn đã nộp phiếu thành công\"}");
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError().body("{\"message\": \"Có lỗi xảy ra: " + e.getMessage() + "\"}");
        }
    }
}
