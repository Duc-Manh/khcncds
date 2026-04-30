package com.khcncds.genco2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class MailService {

    @Autowired
    private JavaMailSender mailSender;

    public void sendApprovalEmail(String toEmail, String username, String password) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(toEmail);
        message.setSubject("Thông báo: Tài khoản của bạn đã được phê duyệt");
        message.setText("Chào bạn,\n\n" +
                "Yêu cầu tạo tài khoản của bạn đã được phê duyệt thành công.\n\n" +
                "Dưới đây là thông tin đăng nhập của bạn:\n" +
                "Tên đăng nhập (Username): " + username + "\n" +
                "Mật khẩu (Password): " + password + "\n\n" +
                "Vui lòng đăng nhập và tiến hành đổi mật khẩu nếu cần.\n\n" +
                "Trân trọng,\n" +
                "Hệ thống KHCNCDS - EVNGENCO2");

        try {
            mailSender.send(message);
        } catch (Exception e) {
            // Log the error but don't crash the application if email fails
            System.err.println("Lỗi khi gửi email đến " + toEmail + ": " + e.getMessage());
        }
    }
}
