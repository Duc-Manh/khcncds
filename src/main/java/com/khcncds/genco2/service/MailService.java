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

    public void sendRejectionEmail(String toEmail) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(toEmail);
        message.setSubject("Thông báo: Đăng ký tài khoản không thành công");
        message.setText("Chào bạn,\n\n" +
                "Yêu cầu tạo tài khoản của bạn trên hệ thống KHCNCDS - EVNGENCO2 không thành công và đã bị từ chối.\n\n" +
                "Vui lòng liên hệ với quản trị viên nếu bạn có bất kỳ thắc mắc nào.\n\n" +
                "Trân trọng,\n" +
                "Hệ thống KHCNCDS - EVNGENCO2");

        try {
            mailSender.send(message);
        } catch (Exception e) {
            System.err.println("Lỗi khi gửi email từ chối đến " + toEmail + ": " + e.getMessage());
        }
    }
    public void sendConsultationEmail(String toEmail) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(toEmail);
        message.setSubject("Thông báo: Bạn có một yêu cầu tham vấn mới");
        message.setText("Chào bạn,\n\n" +
                "Bạn có 1 tham vấn mới từ hệ thống.\n\n" +
                "Vui lòng truy cập vào khcn-evngenco2.vn rồi đăng nhập vào tài khoản chuyên gia để xem và trả lời tham vấn của mình.\n\n" +
                "Trân trọng,\n" +
                "Hệ thống KHCNCDS - EVNGENCO2");

        try {
            mailSender.send(message);
        } catch (Exception e) {
            System.err.println("Lỗi khi gửi email tham vấn đến " + toEmail + ": " + e.getMessage());
        }
    }
}
