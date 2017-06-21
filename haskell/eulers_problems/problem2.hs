fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

list = map fib [1..35]
--arbritrary limit... need to fix

filteredList = filter (\(x) -> (x `mod` 2==0) && (x<4000000)) list

answer = sum(filteredList)
