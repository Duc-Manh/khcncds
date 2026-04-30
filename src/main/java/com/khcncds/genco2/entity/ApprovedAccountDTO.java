package com.khcncds.genco2.entity;

import lombok.Data;
import java.time.LocalDateTime;

@Data
public class ApprovedAccountDTO {
    private Long id;
    private String department;
    private String email;
    private String fullName;
    private String position;
    private String phone;
    private LocalDateTime actionDay; // Maps to approday or councilday
    private String username;
    private String password;
}
