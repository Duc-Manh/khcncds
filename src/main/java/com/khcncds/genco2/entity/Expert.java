package com.khcncds.genco2.entity;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "expert")
public class Expert {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "position")
    private String position;

    @Column(name = "username")
    private String username;

    @Column(name = "password")
    private String password;

    @Column(name = "full_name", nullable = false)
    private String fullName;

    @Column(name = "cccd", nullable = false)
    private String cccd;

    @Column(name = "phone", nullable = false)
    private String phone;

    @Column(name = "email", nullable = false)
    private String email;

    @Column(name = "`rank`") // Escaped reserved keyword
    private String rank;

    @Column(name = "department", nullable = false)
    private String department;

    @Column(name = "major", nullable = false)
    private String major;

    @Column(name = "field")
    private String field;

    @Column(name = "trend", nullable = false)
    private String trend;

    @Column(name = "accept")
    private Integer accept = 0;

    @Column(name = "google", nullable = false)
    private String google;

    @Column(name = "orcid")
    private String orcid;

    @Column(name = "gate")
    private String gate;
}
