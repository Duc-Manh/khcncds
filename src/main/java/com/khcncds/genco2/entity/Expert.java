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

    @Column(name = "google", nullable = false)
    private String google;

    @Column(name = "orcid")
    private String orcid;

    @Column(name = "gate")
    private String gate;
}
