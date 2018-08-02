(define (reverselist lst)
 (if (null? lst)
  '()
					;(reverselist (cons (cdr lst) (car lst))))
  
  (cons (reverselist (cdr lst)) ( (car lst)))
 )
)

(reverselist (list 1 4 9 16 25))

(define x (list (list 1 2) (list 3 4)))
x
(reverselist x)
