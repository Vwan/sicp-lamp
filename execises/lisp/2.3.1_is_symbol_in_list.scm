(define (is-symbol-in-list symbol list)
 (
   cond ((null? list) false)
   ((eq? symbol (car list)) true)
 (else (is-symbol-in-list symbol (cdr list)))
 )

)

(define a 's)
(define b 't)

(is-symbol-in-list a (list 'a 'b))


(is-symbol-in-list 'apple '(pear banana prune))
(is-symbol-in-list 'apple '(x (apple sauce) y apple pear))

(memq 'apple '(pear banana prune))
(memq 'apple '(x (apple sauce) y apple pear))
