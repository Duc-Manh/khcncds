package com.khcncds.genco2.controller;

import com.google.code.kaptcha.impl.DefaultKaptcha;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.IOException;

@Controller
public class CaptchaController {

    @Autowired
    private DefaultKaptcha defaultKaptcha;

    @GetMapping("/captcha")
    public void getCaptcha(HttpSession session, HttpServletResponse response) throws IOException {
        // Cấu hình headers chống cache
        response.setHeader("Cache-Control", "no-store, no-cache, must-revalidate");
        response.addHeader("Cache-Control", "post-check=0, pre-check=0");
        response.setHeader("Pragma", "no-cache");
        response.setContentType("image/jpeg");

        // Sinh chuỗi mã xác thực
        String capText = defaultKaptcha.createText();
        
        // Lưu vào Session để so sánh khi form được submit
        session.setAttribute("CAPTCHA_SESSION_KEY", capText);

        // Vẽ chuỗi thành ảnh và ghi ra OutputStream
        BufferedImage bi = defaultKaptcha.createImage(capText);
        ImageIO.write(bi, "jpg", response.getOutputStream());
        
        try {
            response.getOutputStream().flush();
        } finally {
            response.getOutputStream().close();
        }
    }
}
