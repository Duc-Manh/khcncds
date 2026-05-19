package com.khcncds.genco2.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "comment")
public class Comment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "full_name")
    private String fullName;

    private String department;
    private String position;
    private String phone;
    private String email;

    @Column(name = "time")
    private LocalDateTime time;

    private Integer state;

    @Column(columnDefinition = "TEXT")
    private String i1;

    @Column(columnDefinition = "TEXT")
    private String i2;

    @Column(columnDefinition = "TEXT")
    private String i3;

    @Column(columnDefinition = "TEXT")
    private String i4;

    @Column(columnDefinition = "TEXT")
    private String i5;

    @Column(columnDefinition = "TEXT")
    private String i6;

    @Column(columnDefinition = "TEXT")
    private String i7;

    @Column(columnDefinition = "TEXT")
    private String i8;

    @Column(columnDefinition = "TEXT")
    private String i9;

    @Column(columnDefinition = "TEXT")
    private String i10;

    @Column(columnDefinition = "TEXT")
    private String i11;

    @Column(columnDefinition = "TEXT")
    private String i12;

    @Column(columnDefinition = "TEXT")
    private String i13;

    @Column(columnDefinition = "TEXT")
    private String i14;

    @Column(columnDefinition = "TEXT")
    private String i15;

    @Column(columnDefinition = "TEXT")
    private String i16;

    @Column(columnDefinition = "TEXT")
    private String i17;

    @Column(columnDefinition = "TEXT")
    private String i18;

    @Column(columnDefinition = "TEXT")
    private String i19;

    @Column(columnDefinition = "TEXT")
    private String i20;

    @Column(columnDefinition = "TEXT")
    private String i21;

    @Column(columnDefinition = "TEXT")
    private String i22;

    @Column(columnDefinition = "TEXT")
    private String i23;

    @Column(columnDefinition = "TEXT")
    private String i24;

    @Column(columnDefinition = "TEXT")
    private String i25;

    @Column(columnDefinition = "TEXT")
    private String i26;

    @Column(columnDefinition = "TEXT")
    private String i27;

    @Column(columnDefinition = "TEXT")
    private String i28;

    @Column(columnDefinition = "TEXT")
    private String i29;

    @Column(columnDefinition = "TEXT")
    private String i30;

    @Column(columnDefinition = "TEXT")
    private String i31;

    @Column(columnDefinition = "TEXT")
    private String i32;

    @Column(columnDefinition = "TEXT")
    private String i33;

    @Column(columnDefinition = "TEXT")
    private String i34;

    @Column(columnDefinition = "TEXT")
    private String i35;

    @Column(columnDefinition = "TEXT")
    private String i36;

    @Column(columnDefinition = "TEXT")
    private String i37;

    @Column(columnDefinition = "TEXT")
    private String i38;

    @Column(columnDefinition = "TEXT")
    private String i39;

    @Column(columnDefinition = "TEXT")
    private String i40;

    @Column(columnDefinition = "TEXT")
    private String i41;

    @Column(columnDefinition = "TEXT")
    private String i42;

    @Column(columnDefinition = "TEXT")
    private String i43;

    @Column(columnDefinition = "TEXT")
    private String i44;

    @Column(columnDefinition = "TEXT")
    private String i45;

    @Column(columnDefinition = "TEXT")
    private String i46;

    @Column(columnDefinition = "TEXT")
    private String i47;

    @Column(columnDefinition = "TEXT")
    private String i48;

    @Column(columnDefinition = "TEXT")
    private String i49;

    @Column(columnDefinition = "TEXT")
    private String i50;

    @Column(columnDefinition = "TEXT")
    private String i51;

    @Column(columnDefinition = "LONGTEXT")
    private String i52;

    @Column(columnDefinition = "TEXT")
    private String i53;


    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }
    public String getPosition() { return position; }
    public void setPosition(String position) { this.position = position; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public LocalDateTime getTime() { return time; }
    public void setTime(LocalDateTime time) { this.time = time; }
    public Integer getState() { return state; }
    public void setState(Integer state) { this.state = state; }
    public String getI1() { return i1; }
    public void setI1(String i1) { this.i1 = i1; }
    public String getI2() { return i2; }
    public void setI2(String i2) { this.i2 = i2; }
    public String getI3() { return i3; }
    public void setI3(String i3) { this.i3 = i3; }
    public String getI4() { return i4; }
    public void setI4(String i4) { this.i4 = i4; }
    public String getI5() { return i5; }
    public void setI5(String i5) { this.i5 = i5; }
    public String getI6() { return i6; }
    public void setI6(String i6) { this.i6 = i6; }
    public String getI7() { return i7; }
    public void setI7(String i7) { this.i7 = i7; }
    public String getI8() { return i8; }
    public void setI8(String i8) { this.i8 = i8; }
    public String getI9() { return i9; }
    public void setI9(String i9) { this.i9 = i9; }
    public String getI10() { return i10; }
    public void setI10(String i10) { this.i10 = i10; }
    public String getI11() { return i11; }
    public void setI11(String i11) { this.i11 = i11; }
    public String getI12() { return i12; }
    public void setI12(String i12) { this.i12 = i12; }
    public String getI13() { return i13; }
    public void setI13(String i13) { this.i13 = i13; }
    public String getI14() { return i14; }
    public void setI14(String i14) { this.i14 = i14; }
    public String getI15() { return i15; }
    public void setI15(String i15) { this.i15 = i15; }
    public String getI16() { return i16; }
    public void setI16(String i16) { this.i16 = i16; }
    public String getI17() { return i17; }
    public void setI17(String i17) { this.i17 = i17; }
    public String getI18() { return i18; }
    public void setI18(String i18) { this.i18 = i18; }
    public String getI19() { return i19; }
    public void setI19(String i19) { this.i19 = i19; }
    public String getI20() { return i20; }
    public void setI20(String i20) { this.i20 = i20; }
    public String getI21() { return i21; }
    public void setI21(String i21) { this.i21 = i21; }
    public String getI22() { return i22; }
    public void setI22(String i22) { this.i22 = i22; }
    public String getI23() { return i23; }
    public void setI23(String i23) { this.i23 = i23; }
    public String getI24() { return i24; }
    public void setI24(String i24) { this.i24 = i24; }
    public String getI25() { return i25; }
    public void setI25(String i25) { this.i25 = i25; }
    public String getI26() { return i26; }
    public void setI26(String i26) { this.i26 = i26; }
    public String getI27() { return i27; }
    public void setI27(String i27) { this.i27 = i27; }
    public String getI28() { return i28; }
    public void setI28(String i28) { this.i28 = i28; }
    public String getI29() { return i29; }
    public void setI29(String i29) { this.i29 = i29; }
    public String getI30() { return i30; }
    public void setI30(String i30) { this.i30 = i30; }
    public String getI31() { return i31; }
    public void setI31(String i31) { this.i31 = i31; }
    public String getI32() { return i32; }
    public void setI32(String i32) { this.i32 = i32; }
    public String getI33() { return i33; }
    public void setI33(String i33) { this.i33 = i33; }
    public String getI34() { return i34; }
    public void setI34(String i34) { this.i34 = i34; }
    public String getI35() { return i35; }
    public void setI35(String i35) { this.i35 = i35; }
    public String getI36() { return i36; }
    public void setI36(String i36) { this.i36 = i36; }
    public String getI37() { return i37; }
    public void setI37(String i37) { this.i37 = i37; }
    public String getI38() { return i38; }
    public void setI38(String i38) { this.i38 = i38; }
    public String getI39() { return i39; }
    public void setI39(String i39) { this.i39 = i39; }
    public String getI40() { return i40; }
    public void setI40(String i40) { this.i40 = i40; }
    public String getI41() { return i41; }
    public void setI41(String i41) { this.i41 = i41; }
    public String getI42() { return i42; }
    public void setI42(String i42) { this.i42 = i42; }
    public String getI43() { return i43; }
    public void setI43(String i43) { this.i43 = i43; }
    public String getI44() { return i44; }
    public void setI44(String i44) { this.i44 = i44; }
    public String getI45() { return i45; }
    public void setI45(String i45) { this.i45 = i45; }
    public String getI46() { return i46; }
    public void setI46(String i46) { this.i46 = i46; }
    public String getI47() { return i47; }
    public void setI47(String i47) { this.i47 = i47; }
    public String getI48() { return i48; }
    public void setI48(String i48) { this.i48 = i48; }
    public String getI49() { return i49; }
    public void setI49(String i49) { this.i49 = i49; }
    public String getI50() { return i50; }
    public void setI50(String i50) { this.i50 = i50; }
    public String getI51() { return i51; }
    public void setI51(String i51) { this.i51 = i51; }
    public String getI52() { return i52; }
    public void setI52(String i52) { this.i52 = i52; }
    public String getI53() { return i53; }
    public void setI53(String i53) { this.i53 = i53; }
}
