(define (reverselist lst)
 (if (null? lst)
  '()
  ;(reverselist (cons (cdr lst) (car lst))))
  (append (reverselist (cdr lst)) (flatten (car lst)))
 )
)

(reverselist (list 1 4 9 16 25))
