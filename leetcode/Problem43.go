package leetcode

type Problem43 struct {}

func (p *Problem43) Multiply(num1 string, num2 string) string {
    if num1 == "0" || num2 == "0" {
        return "0"
    }

    n := len(num1)
    m := len(num2)
    
    mult := make([]int, n+m)
    for i:=n-1; i>=0; i-- {
        for j:=m-1; j>=0; j-- {
            mult[i+j+1] += int((num1[i] - '0')) * int((num2[j] - '0'))
        }
    }

    c := 0
    for i := len(mult)-1; i>=0; i-- {
        v := mult[i] + c
        mult[i] = v % 10
        c = v / 10
    }

    var sb strings.Builder
    for _, v := range mult {
        sb.WriteString(strconv.Itoa(v))
    }
    
    return strings.TrimLeft(sb.String(), "0")
}

func main() {
    var p Problem43{}
    fmt.Println(p.Multiply("123", "456"))
}