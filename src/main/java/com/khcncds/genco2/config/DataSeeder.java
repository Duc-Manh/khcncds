package com.khcncds.genco2.config;

import com.khcncds.genco2.entity.UserEntity;
import com.khcncds.genco2.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DataSeeder implements CommandLineRunner {

    @Autowired
    private UserRepository userRepository;

    @Override
    public void run(String... args) throws Exception {
        // Kiểm tra xem tài khoản admin đã tồn tại chưa
        if (userRepository.findByUsername("admin@khcncds").isEmpty()) {
            // Nếu chưa có, tự động tạo tài khoản admin
            UserEntity admin = new UserEntity();
            admin.setUsername("admin@khcncds");
            admin.setPassword("4dm1n@KHCNcds@6202");
            admin.setFullName("Quản trị viên Hệ thống");
            admin.setEmail("admin@evngenco2.vn");
            admin.setDepartment("Ban KHCN");
            admin.setPosition("Trưởng ban");
            
            userRepository.save(admin);
            System.out.println("Đã khởi tạo tài khoản Admin mặc định thành công!");
        }
    }
}
