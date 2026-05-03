package com.khcncds.genco2.service;

import com.khcncds.genco2.entity.RegisterEntity;
import com.khcncds.genco2.entity.ApprovedAccountDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.sql.ResultSet;
import java.time.LocalDateTime;
import java.time.Year;
import java.util.List;

@Service
public class DynamicApproveService {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Autowired
    private MailService mailService;

    @Transactional
    public String[] approveAccount(Long registerId) {
        int currentYear = Year.now().getValue();
        String registerTable = "register" + currentYear;
        String approTable = "appro" + currentYear;

        // 1. Fetch the register record
        String selectSql = "SELECT * FROM " + registerTable + " WHERE id = ?";
        List<RegisterEntity> registers = jdbcTemplate.query(selectSql, (ResultSet rs, int rowNum) -> {
            RegisterEntity entity = new RegisterEntity();
            entity.setId(rs.getLong("id"));
            entity.setDepartment(rs.getString("department"));
            entity.setEmail(rs.getString("email"));
            entity.setFullName(rs.getString("full_name"));
            entity.setPosition(rs.getString("position"));
            entity.setPhone(rs.getString("phone"));
            entity.setAim(rs.getString("aim"));
            return entity;
        }, registerId);

        if (registers.isEmpty()) {
            throw new RuntimeException("Không tìm thấy dữ liệu đăng ký với ID: " + registerId);
        }
        RegisterEntity reg = registers.get(0);

        String username;
        String password;

        if ("Đăng ký xét duyệt".equals(reg.getAim())) {
            String councilTable = "council" + currentYear;
            ensureCouncilTableExists(councilTable);
            username = generateCouncilUsername(reg.getDepartment(), reg.getFullName(), currentYear);
            password = generateCouncilPassword(reg.getFullName(), currentYear);

            String insertSql = "INSERT INTO " + councilTable +
                    " (department, email, full_name, position, phone, councilday, username, password) " +
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
            jdbcTemplate.update(insertSql,
                    reg.getDepartment(),
                    reg.getEmail(),
                    reg.getFullName(),
                    reg.getPosition(),
                    reg.getPhone(),
                    LocalDateTime.now(),
                    username,
                    password);
        } else {
            ensureApproTableExists(approTable);
            username = generateUsername(reg.getDepartment(), reg.getFullName(), currentYear);
            password = "khcncds@123456#";

            String insertSql = "INSERT INTO " + approTable +
                    " (department, email, full_name, position, phone, approday, username, password) " +
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
            jdbcTemplate.update(insertSql,
                    reg.getDepartment(),
                    reg.getEmail(),
                    reg.getFullName(),
                    reg.getPosition(),
                    reg.getPhone(),
                    LocalDateTime.now(),
                    username,
                    password);
        }

        // 5. Delete from register table
        String deleteSql = "DELETE FROM " + registerTable + " WHERE id = ?";
        jdbcTemplate.update(deleteSql, registerId);

        // 6. Send Email
        if (reg.getEmail() != null && !reg.getEmail().isEmpty()) {
            mailService.sendApprovalEmail(reg.getEmail(), username, password);
        }

        return new String[] { username, reg.getAim() };
    }

    public List<ApprovedAccountDTO> getApproAccounts() {
        int currentYear = Year.now().getValue();
        String approTable = "appro" + currentYear;
        try {
            ensureApproTableExists(approTable);
            String sql = "SELECT * FROM " + approTable + " ORDER BY id DESC";
            return jdbcTemplate.query(sql, (rs, rowNum) -> {
                ApprovedAccountDTO dto = new ApprovedAccountDTO();
                dto.setId(rs.getLong("id"));
                dto.setDepartment(rs.getString("department"));
                dto.setEmail(rs.getString("email"));
                dto.setFullName(rs.getString("full_name"));
                dto.setPosition(rs.getString("position"));
                dto.setPhone(rs.getString("phone"));
                dto.setActionDay(
                        rs.getTimestamp("approday") != null ? rs.getTimestamp("approday").toLocalDateTime() : null);
                dto.setUsername(rs.getString("username"));
                dto.setPassword(rs.getString("password"));
                return dto;
            });
        } catch (Exception e) {
            return List.of();
        }
    }

    public List<ApprovedAccountDTO> getCouncilAccounts() {
        int currentYear = Year.now().getValue();
        String councilTable = "council" + currentYear;
        try {
            ensureCouncilTableExists(councilTable);
            String sql = "SELECT * FROM " + councilTable + " ORDER BY id DESC";
            return jdbcTemplate.query(sql, (rs, rowNum) -> {
                ApprovedAccountDTO dto = new ApprovedAccountDTO();
                dto.setId(rs.getLong("id"));
                dto.setDepartment(rs.getString("department"));
                dto.setEmail(rs.getString("email"));
                dto.setFullName(rs.getString("full_name"));
                dto.setPosition(rs.getString("position"));
                dto.setPhone(rs.getString("phone"));
                dto.setActionDay(
                        rs.getTimestamp("councilday") != null ? rs.getTimestamp("councilday").toLocalDateTime() : null);
                dto.setUsername(rs.getString("username"));
                dto.setPassword(rs.getString("password"));
                return dto;
            });
        } catch (Exception e) {
            return List.of();
        }
    }

    public void deleteApproAccount(String username) {
        int currentYear = Year.now().getValue();
        String approTable = "appro" + currentYear;
        try {
            ensureApproTableExists(approTable);
            String deleteSql = "DELETE FROM " + approTable + " WHERE username = ?";
            jdbcTemplate.update(deleteSql, username);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void deleteCouncilAccount(String username) {
        int currentYear = Year.now().getValue();
        String councilTable = "council" + currentYear;
        try {
            ensureCouncilTableExists(councilTable);
            String deleteSql = "DELETE FROM " + councilTable + " WHERE username = ?";
            jdbcTemplate.update(deleteSql, username);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void ensureApproTableExists(String tableName) {
        String createTableSql = "CREATE TABLE IF NOT EXISTS " + tableName + " (" +
                "id BIGINT AUTO_INCREMENT PRIMARY KEY, " +
                "department VARCHAR(255), " +
                "email VARCHAR(255), " +
                "full_name VARCHAR(255), " +
                "position VARCHAR(255), " +
                "phone VARCHAR(255), " +
                "approday DATETIME, " +
                "username VARCHAR(255), " +
                "password VARCHAR(255)" +
                ")";
        jdbcTemplate.execute(createTableSql);
    }

    private void ensureCouncilTableExists(String tableName) {
        String createTableSql = "CREATE TABLE IF NOT EXISTS " + tableName + " (" +
                "id BIGINT AUTO_INCREMENT PRIMARY KEY, " +
                "department VARCHAR(255), " +
                "email VARCHAR(255), " +
                "full_name VARCHAR(255), " +
                "position VARCHAR(255), " +
                "phone VARCHAR(255), " +
                "councilday DATETIME, " +
                "username VARCHAR(255), " +
                "password VARCHAR(255)" +
                ")";
        jdbcTemplate.execute(createTableSql);
    }

    private String generateUsername(String department, String fullName, int year) {
        String deptCode = getDepartmentCode(department);
        return deptCode + "." + getNamePart(fullName) + "." + year;
    }

    private String generateCouncilUsername(String department, String fullName, int year) {
        String deptCode = getDepartmentCode(department);
        return deptCode + ".hdkh." + getNamePart(fullName) + "." + year;
    }

    private String generateCouncilPassword(String fullName, int year) {
        return "hdkh@" + year + "." + getNamePart(fullName);
    }

    private String getNamePart(String fullName) {
        if (fullName == null || fullName.trim().isEmpty()) {
            return "user";
        }

        String[] words = fullName.trim().split("\\s+");
        if (words.length == 0)
            return "user";

        String lastWord = words[words.length - 1].toLowerCase();
        StringBuilder initials = new StringBuilder();
        for (int i = 0; i < words.length - 1; i++) {
            if (!words[i].isEmpty()) {
                initials.append(words[i].toLowerCase().charAt(0));
            }
        }

        return lastWord + initials.toString();
    }

    private String getDepartmentCode(String department) {
        if (department == null)
            return "unk";
        String lower = department.toLowerCase();

        if (lower.contains("cơ quan tổng công ty") || lower.contains("phát điện 2") || lower.contains("genco2"))
            return "ge2";
        if (lower.contains("nhiệt điện cần thơ"))
            return "ct";
        if (lower.contains("an khê"))
            return "ak";
        if (lower.contains("quảng trị"))
            return "qt";
        if (lower.contains("sông bung"))
            return "sb";
        if (lower.contains("trung sơn"))
            return "ts";
        if (lower.contains("thác mơ"))
            return "tm";
        if (lower.contains("a vương"))
            return "av";
        if (lower.contains("sông ba hạ"))
            return "sbh";
        if (lower.contains("phả lại"))
            return "pl";
        if (lower.contains("hải phòng"))
            return "hp";

        return "unk";
    }

    public boolean validateApproUser(String username, String password) {
        int currentYear = Year.now().getValue();
        String approTable = "appro" + currentYear;

        try {
            ensureApproTableExists(approTable);

            String selectSql = "SELECT count(*) FROM " + approTable + " WHERE username = ? AND password = ?";
            Integer count = jdbcTemplate.queryForObject(selectSql, Integer.class, username, password);
            return count != null && count > 0;
        } catch (Exception e) {
            // If table doesn't exist or any other DB issue, return false
            return false;
        }
    }

    public boolean validateCouncilUser(String username, String password) {
        int currentYear = Year.now().getValue();
        String councilTable = "council" + currentYear;

        try {
            ensureCouncilTableExists(councilTable);

            String selectSql = "SELECT count(*) FROM " + councilTable + " WHERE username = ? AND password = ?";
            Integer count = jdbcTemplate.queryForObject(selectSql, Integer.class, username, password);
            return count != null && count > 0;
        } catch (Exception e) {
            // If table doesn't exist or any other DB issue, return false
            return false;
        }
    }
}
