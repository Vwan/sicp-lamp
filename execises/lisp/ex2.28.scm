(define (fringe lst)
 (cond ((null? lst)  '())
  ((not (pair? lst) ) lst)
  (else (append (fringe (flatten (car lst))) (flatten(fringe (cdr lst)))))
 )
)

(define x (list (list 1 2) (list 3 4)))
(fringe x)   ; not work yet
;(1 2 3 4)
(fringe (list x x))
;(1 2 3 4 1 2 3 4)