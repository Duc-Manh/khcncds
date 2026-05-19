package com.khcncds.genco2.repository;

import com.khcncds.genco2.entity.Comment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CommentRepository extends JpaRepository<Comment, Long> {
    java.util.List<Comment> findByFullNameOrderByTimeDesc(String fullName);
}
