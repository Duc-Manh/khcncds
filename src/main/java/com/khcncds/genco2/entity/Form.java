package com.khcncds.genco2.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.Column;
import jakarta.persistence.Lob;
import java.time.LocalDateTime;

@Entity
@Table(name = "form")
public class Form {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime time;
    private String department;
    private String position;
    
    @Column(name = "full_name")
    private String fullName;
    private String phone;
    private String email;

    @Lob @Column(columnDefinition="LONGTEXT") private String in1;
    @Lob @Column(columnDefinition="LONGTEXT") private String in2;
    @Lob @Column(columnDefinition="LONGTEXT") private String in3;
    @Lob @Column(columnDefinition="LONGTEXT") private String in4;
    @Lob @Column(columnDefinition="LONGTEXT") private String in5;
    @Lob @Column(columnDefinition="LONGTEXT") private String in6;
    @Lob @Column(columnDefinition="LONGTEXT") private String in7;
    @Lob @Column(columnDefinition="LONGTEXT") private String in8;
    @Lob @Column(columnDefinition="LONGTEXT") private String in9;
    @Lob @Column(columnDefinition="LONGTEXT") private String in10;
    @Lob @Column(columnDefinition="LONGTEXT") private String in11;
    @Lob @Column(columnDefinition="LONGTEXT") private String in12;
    @Lob @Column(columnDefinition="LONGTEXT") private String in13;
    @Lob @Column(columnDefinition="LONGTEXT") private String in14;
    @Lob @Column(columnDefinition="LONGTEXT") private String in15;
    @Lob @Column(columnDefinition="LONGTEXT") private String in16;
    @Lob @Column(columnDefinition="LONGTEXT") private String in17;
    @Lob @Column(columnDefinition="LONGTEXT") private String in18;
    @Lob @Column(columnDefinition="LONGTEXT") private String in19;
    @Lob @Column(columnDefinition="LONGTEXT") private String in20;
    @Lob @Column(columnDefinition="LONGTEXT") private String in21;
    @Lob @Column(columnDefinition="LONGTEXT") private String in22;
    @Lob @Column(columnDefinition="LONGTEXT") private String in23;
    @Lob @Column(columnDefinition="LONGTEXT") private String in24;
    @Lob @Column(columnDefinition="LONGTEXT") private String in25;
    @Lob @Column(columnDefinition="LONGTEXT") private String in26;
    @Lob @Column(columnDefinition="LONGTEXT") private String in27;
    @Lob @Column(columnDefinition="LONGTEXT") private String in28;
    @Lob @Column(columnDefinition="LONGTEXT") private String in29;
    @Lob @Column(columnDefinition="LONGTEXT") private String in30;
    @Lob @Column(columnDefinition="LONGTEXT") private String in31;
    @Lob @Column(columnDefinition="LONGTEXT") private String in32;
    @Lob @Column(columnDefinition="LONGTEXT") private String in33;
    @Lob @Column(columnDefinition="LONGTEXT") private String in34;
    @Lob @Column(columnDefinition="LONGTEXT") private String in35;
    @Lob @Column(columnDefinition="LONGTEXT") private String in36;

    private Integer state;

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public LocalDateTime getTime() { return time; }
    public void setTime(LocalDateTime time) { this.time = time; }
    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }
    public String getPosition() { return position; }
    public void setPosition(String position) { this.position = position; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public Integer getState() { return state; }
    public void setState(Integer state) { this.state = state; }

    public String getIn1() { return in1; } public void setIn1(String in1) { this.in1 = in1; }
    public String getIn2() { return in2; } public void setIn2(String in2) { this.in2 = in2; }
    public String getIn3() { return in3; } public void setIn3(String in3) { this.in3 = in3; }
    public String getIn4() { return in4; } public void setIn4(String in4) { this.in4 = in4; }
    public String getIn5() { return in5; } public void setIn5(String in5) { this.in5 = in5; }
    public String getIn6() { return in6; } public void setIn6(String in6) { this.in6 = in6; }
    public String getIn7() { return in7; } public void setIn7(String in7) { this.in7 = in7; }
    public String getIn8() { return in8; } public void setIn8(String in8) { this.in8 = in8; }
    public String getIn9() { return in9; } public void setIn9(String in9) { this.in9 = in9; }
    public String getIn10() { return in10; } public void setIn10(String in10) { this.in10 = in10; }
    public String getIn11() { return in11; } public void setIn11(String in11) { this.in11 = in11; }
    public String getIn12() { return in12; } public void setIn12(String in12) { this.in12 = in12; }
    public String getIn13() { return in13; } public void setIn13(String in13) { this.in13 = in13; }
    public String getIn14() { return in14; } public void setIn14(String in14) { this.in14 = in14; }
    public String getIn15() { return in15; } public void setIn15(String in15) { this.in15 = in15; }
    public String getIn16() { return in16; } public void setIn16(String in16) { this.in16 = in16; }
    public String getIn17() { return in17; } public void setIn17(String in17) { this.in17 = in17; }
    public String getIn18() { return in18; } public void setIn18(String in18) { this.in18 = in18; }
    public String getIn19() { return in19; } public void setIn19(String in19) { this.in19 = in19; }
    public String getIn20() { return in20; } public void setIn20(String in20) { this.in20 = in20; }
    public String getIn21() { return in21; } public void setIn21(String in21) { this.in21 = in21; }
    public String getIn22() { return in22; } public void setIn22(String in22) { this.in22 = in22; }
    public String getIn23() { return in23; } public void setIn23(String in23) { this.in23 = in23; }
    public String getIn24() { return in24; } public void setIn24(String in24) { this.in24 = in24; }
    public String getIn25() { return in25; } public void setIn25(String in25) { this.in25 = in25; }
    public String getIn26() { return in26; } public void setIn26(String in26) { this.in26 = in26; }
    public String getIn27() { return in27; } public void setIn27(String in27) { this.in27 = in27; }
    public String getIn28() { return in28; } public void setIn28(String in28) { this.in28 = in28; }
    public String getIn29() { return in29; } public void setIn29(String in29) { this.in29 = in29; }
    public String getIn30() { return in30; } public void setIn30(String in30) { this.in30 = in30; }
    public String getIn31() { return in31; } public void setIn31(String in31) { this.in31 = in31; }
    public String getIn32() { return in32; } public void setIn32(String in32) { this.in32 = in32; }
    public String getIn33() { return in33; } public void setIn33(String in33) { this.in33 = in33; }
    public String getIn34() { return in34; } public void setIn34(String in34) { this.in34 = in34; }
    public String getIn35() { return in35; } public void setIn35(String in35) { this.in35 = in35; }
    public String getIn36() { return in36; } public void setIn36(String in36) { this.in36 = in36; }
}
