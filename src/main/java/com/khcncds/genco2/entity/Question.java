package com.khcncds.genco2.entity;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "question")
public class Question {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime time;

    @Column(name = "full_name")
    private String fullName;

    private String department;
    private String position;
    private String phone;
    private String email;
    
    private String title;
    
    @Column(columnDefinition = "TEXT")
    private String question;

    @Column(name = "cg_rank")
    private String cgRank;

    @Column(name = "cg_full_name")
    private String cgFullName;

    @Column(name = "cg_department")
    private String cgDepartment;

    @Column(name = "cg_position")
    private String cgPosition;

    @Column(name = "cg_field")
    private String cgField;

    @Column(name = "cg_phone")
    private String cgPhone;

    @Column(name = "cg_email")
    private String cgEmail;

    @Column(name = "cg_answer", columnDefinition = "TEXT")
    private String cgAnswer;

    private String state;
}
