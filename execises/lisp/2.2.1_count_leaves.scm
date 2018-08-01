; define length to get size of a list
(define (length lst)
 (cond ( (null? lst)      0)
  ( (+ 1 (length (cdr lst))))
 )
)

(define (count-leaves lst)
 (cond
  ((null? lst) 0)   ; 之前错将lst写成list，结果将树的顶点都计算在内了

        ((not (pair? lst))      1    ) ;判断是否是list，如果不是，则是叶子，计入
  (else (+ (count-leaves (car lst)) (count-leaves (cdr lst))))

 )
)

(define x (cons (list 1 2) (list 3 4)))
(length x)
(count-leaves x)



