package com.khcncds.genco2.repository;

import com.khcncds.genco2.entity.Expert;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import java.util.Optional;

@Repository
public interface ExpertRepository extends JpaRepository<Expert, Long> {
    Optional<Expert> findFirstByUsername(String username);
    Page<Expert> findByField(String field, Pageable pageable);
}
