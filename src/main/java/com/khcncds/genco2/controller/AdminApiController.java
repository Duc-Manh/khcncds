package com.khcncds.genco2.controller;

import com.khcncds.genco2.service.StatisticsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collections;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/statistics")
public class AdminApiController {

    @Autowired
    private StatisticsService statisticsService;

    @GetMapping("/years")
    public List<Integer> getAvailableYears(@RequestParam("category") String category) {
        String prefix = getTablePrefix(category);
        if (prefix == null) {
            return Collections.emptyList();
        }
        List<Integer> years = statisticsService.getAvailableYears(prefix);
        // Sort descending
        years.sort(Collections.reverseOrder());
        return years;
    }

    @GetMapping("/data")
    public Map<String, Integer> getStatisticsData(@RequestParam("category") String category, @RequestParam("year") int year) {
        String prefix = getTablePrefix(category);
        if (prefix == null) {
            return Collections.emptyMap();
        }
        String tableName = prefix + year;
        return statisticsService.getDepartmentStats(tableName);
    }

    @GetMapping("/accounts")
    public List<Map<String, String>> getAccounts(@RequestParam("category") String category, @RequestParam("year") int year, @RequestParam("department") String department) {
        String prefix = getTablePrefix(category);
        if (prefix == null) {
            return Collections.emptyList();
        }
        String tableName = prefix + year;
        return statisticsService.getAccountsByDepartment(tableName, department);
    }

    private String getTablePrefix(String category) {
        switch (category) {
            case "Đăng ký tài khoản":
                return "register";
            case "Tài khoản đăng ký sáng kiến":
                return "appro";
            case "Tài khoản hội đồng khoa học":
                return "council";
            case "Chuyên gia":
                return "expert";
            default:
                return null;
        }
    }
}
