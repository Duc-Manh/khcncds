package com.khcncds.genco2.repository;

import com.khcncds.genco2.entity.Form;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FormRepository extends JpaRepository<Form, Long> {
    Form findFirstByOrderByIdDesc();
    
    long countByState(Integer state);
    
    java.util.List<Form> findByState(Integer state);
}
