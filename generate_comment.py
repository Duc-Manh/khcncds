import os

entity_content = """package com.khcncds.genco2.entity;

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

"""

for i in range(1, 54):
    if i == 52:
        entity_content += f'    @Column(columnDefinition = "LONGTEXT")\n'
    else:
        entity_content += f'    @Column(columnDefinition = "TEXT")\n'
    entity_content += f'    private String i{i};\n\n'

entity_content += """
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
"""

for i in range(1, 54):
    entity_content += f'    public String getI{i}() {{ return i{i}; }}\n'
    entity_content += f'    public void setI{i}(String i{i}) {{ this.i{i} = i{i}; }}\n'

entity_content += "}\n"

with open("/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/java/com/khcncds/genco2/entity/Comment.java", "w") as f:
    f.write(entity_content)

repo_content = """package com.khcncds.genco2.repository;

import com.khcncds.genco2.entity.Comment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CommentRepository extends JpaRepository<Comment, Long> {
}
"""

with open("/Users/ducmanh/Documents/3.Project/genco2/genco2/src/main/java/com/khcncds/genco2/repository/CommentRepository.java", "w") as f:
    f.write(repo_content)

