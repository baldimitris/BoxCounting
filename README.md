# BoxCounting
The Box Counting method calculates the Fractal Dimension of an image. It is a way to quantify the complexity and self-similarity of irregular shapes. The algorithm reads a 1024x1024 PNG image and returns its Fractal Dimension.

The algorithm was tested on fractal images of known dimension as shown in the table below.

| Fractal Name          | Theoretical fractal dimension  |  Calculated fractal dimension |
| --- | --- | --- |
| Sierpinski  Triangle  | 1.585 | 1.582 |  
| Koch Curve            | 1.262 | 1.263 |  
| Koch Snowflake        | 1.262 | 1.572 |  
| Gosper  Island        | 1.129 | 1.275 |
| Douady Rabbit         | 1.393 | 1.477 |
| Vicsek fractal        | 1.465 | 1.466 |
| Sierpinski hexagon    | 1.631 | 1.708 |
| Apollonian gasket     | 1.306 | 1.248 | 
