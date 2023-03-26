package com.booklet.bookservice.service;

import com.booklet.bookservice.entity.Book;
import com.booklet.bookservice.entity.Review;
import org.springframework.data.domain.Pageable;

import java.util.HashMap;

public interface ReviewService {
    /** find,save, delete, update */
    public Review findReviewEntity(Long reviewId); // 리뷰 하나 조회
    public HashMap<String, Object> findReviews(Book book, Pageable pageable);    // 책의 리뷰 리스트 반환
    public boolean saveReview(); // 리뷰 작성
    public boolean updateReview(Long reviewId); // 리뷰 수정
    public boolean deleteReview(Long reviewId); // 리뷰 삭제
}
