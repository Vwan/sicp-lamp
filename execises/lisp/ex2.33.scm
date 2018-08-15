(define (accumulate op initial sequence)
(if (null? sequence)
initial
(op (car sequence)
(accumulate op initial (cdr sequence)))))
(accumulate + 0 (list 1 2 3 4 5))

(define (map p sequence)
(accumulate (lambda (x y) (p x y)) nil sequence))

(define (append seq1 seq2)
(accumulate cons ⟨??⟩ ⟨??⟩))

(define (length sequence)
(accumulate ⟨??⟩ 0 sequence))