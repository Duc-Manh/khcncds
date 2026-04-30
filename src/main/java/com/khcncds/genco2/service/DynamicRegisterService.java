package com.khcncds.genco2.service;

import com.khcncds.genco2.entity.RegisterEntity;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.sql.ResultSet;
import java.time.LocalDateTime;
import java.time.Year;
import java.util.List;

@Service
public class DynamicRegisterService {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public void saveRegister(String department, String position, String fullName, String aim, String email, String phone) {
        int currentYear = Year.now().getValue();
        String tableName = "register" + currentYear;

        ensureTableAndColumns(tableName);

        // Insert record
        String insertSql = "INSERT INTO " + tableName + " (aim, department, email, full_name, position, phone, regisday) VALUES (?, ?, ?, ?, ?, ?, ?)";
        jdbcTemplate.update(insertSql, aim, department, email, fullName, position, phone, LocalDateTime.now());
    }

    public List<RegisterEntity> findAllRegistersForCurrentYear() {
        int currentYear = Year.now().getValue();
        String tableName = "register" + currentYear;

        ensureTableAndColumns(tableName);

        String selectSql = "SELECT * FROM " + tableName;
        return jdbcTemplate.query(selectSql, (ResultSet rs, int rowNum) -> {
            RegisterEntity entity = new RegisterEntity();
            entity.setId(rs.getLong("id"));
            entity.setAim(rs.getString("aim"));
            entity.setDepartment(rs.getString("department"));
            entity.setEmail(rs.getString("email"));
            entity.setFullName(rs.getString("full_name"));
            entity.setPosition(rs.getString("position"));
            entity.setPhone(rs.getString("phone"));
            
            java.sql.Timestamp timestamp = rs.getTimestamp("regisday");
            if (timestamp != null) {
                entity.setRegisday(timestamp.toLocalDateTime());
            }
            return entity;
        });
    }

    private void ensureTableAndColumns(String tableName) {
        String createTableSql = "CREATE TABLE IF NOT EXISTS " + tableName + " (" +
                "id BIGINT AUTO_INCREMENT PRIMARY KEY, " +
                "aim VARCHAR(255), " +
                "department VARCHAR(255), " +
                "email VARCHAR(255), " +
                "full_name VARCHAR(255), " +
                "position VARCHAR(255), " +
                "phone VARCHAR(255), " +
                "regisday DATETIME" +
                ")";
        jdbcTemplate.execute(createTableSql);

        // Đảm bảo cột phone tồn tại (phòng trường hợp bảng đã được tạo trước khi thêm tính năng số điện thoại)
        try {
            jdbcTemplate.execute("ALTER TABLE " + tableName + " ADD COLUMN phone VARCHAR(255)");
        } catch (Exception e) {
            // Cột có thể đã tồn tại, bỏ qua lỗi
        }
    }
}
