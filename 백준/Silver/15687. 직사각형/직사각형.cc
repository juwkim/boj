class Rectangle {
private:
    int m_width, m_height;
public:
    Rectangle(int width, int height) :
        m_width(width),
        m_height(height)
    {
    }
    int get_width() const {
        return m_width;
    }
    int get_height() const {
        return m_height;
    }
    void set_width(int width) {
        if ((0 < width) && (width <= 1000))
           m_width = width;
    }
    void set_height(int height) {
        if ((0 < height) && (height <= 2000))
            m_height = height;
    }
    int area() const {
        return m_width * m_height;
    }
    int perimeter() const {
        return 2 * (m_width + m_height);
    }
    bool is_square() const {
        return m_width == m_height;
    }
};