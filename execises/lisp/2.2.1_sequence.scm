(define (list-ref lst n)

  (cond
   ((= n 0) (car lst))
   (else (list-ref (cdr lst))
   )

  )

(list-ref (list 1 2 3 4) 2)
