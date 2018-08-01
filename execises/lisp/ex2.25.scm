(define (pick-number lst n)
 (
   cond ((null? lst) nil)
   ((and (= (car lst) n) (not (pair? (car lst)))) n)
   (else (pick-number (cdr lst) n))
 )
)
; to add condition for (car lst) is a list not a number

(pick-number '( 1 3 ( 5 7) 9) 7)
((7))
(1 (2 (3 (4 (5 (6 7))))))