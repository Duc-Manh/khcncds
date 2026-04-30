package com.khcncds.genco2.config;

import com.google.code.kaptcha.impl.DefaultKaptcha;
import com.google.code.kaptcha.util.Config;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.Properties;

@Configuration
public class CaptchaConfig {

    @Bean
    public DefaultKaptcha getDefaultKaptcha() {
        DefaultKaptcha defaultKaptcha = new DefaultKaptcha();
        Properties properties = new Properties();

        // Cấu hình viền ảnh
        properties.setProperty("kaptcha.border", "no");

        // Màu chữ, kích thước
        properties.setProperty("kaptcha.textproducer.font.color", "41,52,143"); // evnBlue: #29348f -> 41,52,143
        properties.setProperty("kaptcha.textproducer.font.size", "36");
        properties.setProperty("kaptcha.textproducer.font.names", "Arial, Courier, monospace");

        // Chiều dài chuỗi, bộ ký tự
        properties.setProperty("kaptcha.textproducer.char.length", "4");
        properties.setProperty("kaptcha.textproducer.char.string", "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ");

        // Kích thước ảnh (khớp với width-32 h-[50px] của giao diện cũ ~ 128x50)
        properties.setProperty("kaptcha.image.width", "128");
        properties.setProperty("kaptcha.image.height", "50");

        // Đường nhiễu (noise) và hiệu ứng làm méo
        properties.setProperty("kaptcha.noise.color", "gray");
        properties.setProperty("kaptcha.obscurificator.impl", "com.google.code.kaptcha.impl.WaterRipple");

        Config config = new Config(properties);
        defaultKaptcha.setConfig(config);

        return defaultKaptcha;
    }
}
