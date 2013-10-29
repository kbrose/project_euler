;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname p19) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
;; Date structure definition
(define-struct date
  (day month year))

;; Today
(define today
  (make-date 11 10 2011))

; isLeap? function will determine whether or not it is 
;     a leap year based off the input year number
; isLeap? : num -> boolean

(define (isLeap? year-number)
  (cond
     [(integer? (/ year-number 400)) true]
     [(and (integer? (/ year-number 4)) (integer? (/ year-number 100))) false]
     [(integer? (/ year-number 4)) true]
     [else false]))

(check-expect (isLeap? 2004) true)
(check-expect (isLeap? 2000) true)
(check-expect (isLeap? 1900) false)
(check-expect (isLeap? 1990) false)

; fiddle will compute the adjustment value based on the input month and year
; fiddle: num num -> num

(define (fiddle m y)
  (cond
    [(and (equal? m 1) (equal? (isLeap? y) true)) 0]
    [(equal? m 1) 1]
    [(and (equal? m 2) (equal? (isLeap? y) true)) 3]
    [(equal? m 2) 4]
    [(equal? m 3) 4]
    [(equal? m 4) 0]
    [(equal? m 5) 2]
    [(equal? m 6) 5]
    [(equal? m 7) 0]
    [(equal? m 8) 3]
    [(equal? m 9) 6]
    [(equal? m 10) 1]
    [(equal? m 11) 4]
    [(equal? m 12) 6]))

(check-expect (fiddle 1 2000) 0)
(check-expect (fiddle 1 1999) 1)
(check-expect (fiddle 2 1996) 3)
(check-expect (fiddle 2 1901) 4)
(check-expect (fiddle 12 2401) 6)
(check-expect (fiddle 12 2400) 6)
(check-expect (fiddle 8 2011) 3)

; my-day-of-week will take a structure date (day, month, year) and 
;     output the day of the week as a number
; my-day-of-week : date -> num

(define (my-day-of-week adate)
  (modulo
   (+
    (fiddle (date-month adate) (date-year adate))
    (date-day adate)
    (- (date-year adate) 1900)
    (floor (/ (- (date-year adate) 1900) 4))) 7))

(check-expect (my-day-of-week (make-date 12 10 2011)) 4)
(check-expect (my-day-of-week today) 3)
(check-expect (my-day-of-week (make-date 13 10 2011)) 5)
(check-expect (my-day-of-week (make-date 12 3 2000)) 1)
(check-expect (my-day-of-week (make-date 26 6 1995)) 2)

; my-test will take a starting date and count the number of sundays that
;     fall on the first of a month up through dec 31 2000
; my-test : date -> num

(define (my-test adate)
  (cond
    [(equal? (date-year adate) 2001) 0]
    [(equal? (date-month adate) 12)
     (cond
       [(equal? (my-day-of-week adate) 1) 
        (+
         (my-test (make-date 1 1 (+
                                  (date-year adate)
                                  1)))
         1)]
       [else (my-test (make-date 1 1 (+
                                     (date-year adate)
                                     1)))])]
    [(equal? (my-day-of-week adate) 1) 
     (+
      (my-test (make-date 1
                          (+ (date-month adate)
                             1)
                          (date-year adate)))
      1)]
    [else (my-test (make-date 1
                              (+ (date-month adate)
                                 1)
                              (date-year adate)))]))

(my-test (make-date 1 1 1901))

