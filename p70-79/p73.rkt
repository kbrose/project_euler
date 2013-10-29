;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname p73) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ())))
(define (recurse An Ad Bn Bd Dlim)
  (cond
    [(> (+ Ad Bd) Dlim) 0]
    [else (+ (+ (recurse An Ad (+ An Bn) (+ Ad Bd) Dlim)
                (recurse Bn Bd (+ An Bn) (+ Ad Bd) Dlim))
             1)]))
(time (recurse 1 3 1 2 12000))