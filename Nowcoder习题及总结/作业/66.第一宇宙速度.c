/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 计算星球的第一宇宙速度
 * @param M double浮点型 星球的质量
 * @param r double浮点型 星球的半径
 * @return double浮点型
 */
double firstSpeed(double M, double r ) {
    // write code here
    double G = 6.67e-11;//*e是指数英文单词的缩写，代表*10，结合后面的-11，即为10的负11次方
    double v = sqrt(G * M / r);
     return v; 
}