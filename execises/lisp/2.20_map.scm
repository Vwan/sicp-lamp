(define (map func items)
 (
   if (null? items)
     nil
   (cons (func (car items))
    (map func (cdr items)))
 )
)