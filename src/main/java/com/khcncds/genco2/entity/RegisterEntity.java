package com.khcncds.genco2.entity;

import lombok.Data;
import java.time.LocalDateTime;

@Data
public class RegisterEntity {

    private Long id;

    private LocalDateTime regisday;

    private String department;
    
    private String position;
    
    private String email;

    private String fullName;
    
    private String phone;
    
    private String aim;

}
