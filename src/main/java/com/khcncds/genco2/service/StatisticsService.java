package com.khcncds.genco2.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Service
public class StatisticsService {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public List<Integer> getAvailableYears(String prefix) {
        List<Integer> years = new ArrayList<>();
        try {
            String query = "SHOW TABLES LIKE '" + prefix + "20%'";
            List<String> tables = jdbcTemplate.queryForList(query, String.class);
            Pattern pattern = Pattern.compile(prefix + "(\\d{4})");
            for (String table : tables) {
                Matcher matcher = pattern.matcher(table);
                if (matcher.matches()) {
                    years.add(Integer.parseInt(matcher.group(1)));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return years;
    }

    public Map<String, Integer> getDepartmentStats(String tableName) {
        Map<String, Integer> stats = new HashMap<>();
        // Khởi tạo các giá trị mặc định là 0 cho 11 đơn vị
        initDefaultDepartments(stats);

        try {
            // Check if table exists before querying
            String checkTableSql = "SHOW TABLES LIKE '" + tableName + "'";
            List<String> tables = jdbcTemplate.queryForList(checkTableSql, String.class);
            if (tables.isEmpty()) {
                return stats;
            }

            String sql = "SELECT department, count(*) as cnt FROM " + tableName + " GROUP BY department";
            jdbcTemplate.query(sql, (rs, rowNum) -> {
                String rawDepartment = rs.getString("department");
                int count = rs.getInt("cnt");
                String normalizedDept = normalizeDepartmentName(rawDepartment);
                
                if (stats.containsKey(normalizedDept)) {
                    stats.put(normalizedDept, stats.get(normalizedDept) + count);
                }
                return null;
            });
        } catch (Exception e) {
            e.printStackTrace();
        }
        return stats;
    }

    private void initDefaultDepartments(Map<String, Integer> stats) {
        stats.put("Cơ quan Tổng công ty Phát điện 2", 0);
        stats.put("Công ty Nhiệt điện Cần Thơ", 0);
        stats.put("Công ty Thuỷ điện An Khê - Ka Nak", 0);
        stats.put("Công ty Thuỷ điện Quảng Trị", 0);
        stats.put("Công ty Thuỷ điện Sông Bung", 0);
        stats.put("Công ty Thuỷ điện Trung Sơn", 0);
        stats.put("Công ty CP Thuỷ điện Thác Mơ", 0);
        stats.put("Công ty CP Thuỷ điện A Vương", 0);
        stats.put("Công ty CP Thuỷ điện Sông Ba Hạ", 0);
        stats.put("Công ty CP Nhiệt điện Phả Lại", 0);
        stats.put("Công ty CP Nhiệt điện Hải Phòng", 0);
    }

    private String normalizeDepartmentName(String rawDepartment) {
        if (rawDepartment == null) return "Unknown";
        String lower = rawDepartment.toLowerCase();

        if (lower.contains("tổng công ty") || lower.contains("phát điện 2") || lower.contains("genco2")) {
            return "Cơ quan Tổng công ty Phát điện 2";
        }
        if (lower.contains("cần thơ")) return "Công ty Nhiệt điện Cần Thơ";
        if (lower.contains("an khê") || lower.contains("ka nak")) return "Công ty Thuỷ điện An Khê - Ka Nak";
        if (lower.contains("quảng trị")) return "Công ty Thuỷ điện Quảng Trị";
        if (lower.contains("sông bung")) return "Công ty Thuỷ điện Sông Bung";
        if (lower.contains("trung sơn")) return "Công ty Thuỷ điện Trung Sơn";
        if (lower.contains("thác mơ")) return "Công ty CP Thuỷ điện Thác Mơ";
        if (lower.contains("a vương")) return "Công ty CP Thuỷ điện A Vương";
        if (lower.contains("sông ba hạ")) return "Công ty CP Thuỷ điện Sông Ba Hạ";
        if (lower.contains("phả lại")) return "Công ty CP Nhiệt điện Phả Lại";
        if (lower.contains("hải phòng")) return "Công ty CP Nhiệt điện Hải Phòng";

        return rawDepartment;
    }

    public List<Map<String, String>> getAccountsByDepartment(String tableName, String department) {
        List<Map<String, String>> accounts = new ArrayList<>();
        try {
            // Check if table exists
            String checkTableSql = "SHOW TABLES LIKE '" + tableName + "'";
            List<String> tables = jdbcTemplate.queryForList(checkTableSql, String.class);
            if (tables.isEmpty()) {
                return accounts;
            }

            // Mapped based on normalized name checking
            String sql;
            Object[] params;

            if ("Cơ quan Tổng công ty Phát điện 2".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + 
                      " WHERE department LIKE '%Tổng công ty%' OR department LIKE '%Phát điện 2%' OR department LIKE '%GENCO2%'";
                params = new Object[]{};
            } else if ("Công ty Nhiệt điện Cần Thơ".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Cần Thơ%'";
                params = new Object[]{};
            } else if ("Công ty Thuỷ điện An Khê - Ka Nak".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%An Khê%' OR department LIKE '%Ka Nak%'";
                params = new Object[]{};
            } else if ("Công ty Thuỷ điện Quảng Trị".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Quảng Trị%'";
                params = new Object[]{};
            } else if ("Công ty Thuỷ điện Sông Bung".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Sông Bung%'";
                params = new Object[]{};
            } else if ("Công ty Thuỷ điện Trung Sơn".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Trung Sơn%'";
                params = new Object[]{};
            } else if ("Công ty CP Thuỷ điện Thác Mơ".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Thác Mơ%'";
                params = new Object[]{};
            } else if ("Công ty CP Thuỷ điện A Vương".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%A Vương%'";
                params = new Object[]{};
            } else if ("Công ty CP Thuỷ điện Sông Ba Hạ".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Sông Ba Hạ%'";
                params = new Object[]{};
            } else if ("Công ty CP Nhiệt điện Phả Lại".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Phả Lại%'";
                params = new Object[]{};
            } else if ("Công ty CP Nhiệt điện Hải Phòng".equals(department)) {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department LIKE '%Hải Phòng%'";
                params = new Object[]{};
            } else {
                sql = "SELECT full_name, position, phone FROM " + tableName + " WHERE department = ?";
                params = new Object[]{department};
            }

            jdbcTemplate.query(sql, params, (rs, rowNum) -> {
                Map<String, String> acc = new HashMap<>();
                acc.put("fullName", rs.getString("full_name"));
                acc.put("position", rs.getString("position"));
                acc.put("phone", rs.getString("phone"));
                accounts.add(acc);
                return null;
            });
        } catch (Exception e) {
            e.printStackTrace();
        }
        return accounts;
    }
}
