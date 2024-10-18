# Phân tích tình hình chiến dịch tiếp thị SEO của công ty UNIACE

**Link Notion**: https://south-fine-1b1.notion.site/Project-3-Ph-n-t-ch-t-nh-h-nh-chi-n-d-ch-ti-p-th-SEO-c-a-c-ng-ty-UNIACE-1237359e5f5880ebb4c3c0e77784fe2a?pvs=4

# 1. TỔNG QUAN VỀ CÔNG TY VÀ CHIẾN DỊCH TIẾP THỊ SEO

Công ty TNHH **UNIACE** là một đơn vị chuyên về **lĩnh vực giáo dục**, với sứ mệnh cung cấp các **khóa học và kiến thức sâu rộng** liên quan đến **Khoa học Dữ liệu**. Nhằm gia tăng **nhận diện thương hiệu** và tiếp cận đối tượng khách hàng mục tiêu, công ty đã triển khai một **chiến dịch Tiếp thị SEO** vào ngày **1 tháng 8 năm 2022**. Mục tiêu chính của chiến dịch này là **tối ưu hóa khả năng hiển thị** của website trên các công cụ tìm kiếm và **nâng cao trải nghiệm người dùng**.

**Báo cáo này** cung cấp một **cái nhìn toàn diện** về tình hình **chiến dịch Tiếp thị SEO** của công ty UNIACE, từ đó giúp doanh nghiệp phân tích được các yếu tố quan trọng như:

- **Xu hướng tìm kiếm**
- **Từ khóa phổ biến**
- **Hành vi truy cập của khách hàng**

Việc phân tích này giúp UNIACE hiểu rõ hơn về **nhu cầu**, **sở thích** của khách hàng tiềm năng và tạo điều kiện thuận lợi cho việc:

- **Cải thiện chiến lược nội dung**
- **Tối ưu hóa trải nghiệm người dùng** trên website

Chiến dịch tập trung vào việc **tối ưu hóa các từ khóa** liên quan đến **Khoa học Dữ liệu** và **kỹ năng làm việc**, với hy vọng thu hút **sự quan tâm** lớn hơn từ **sinh viên** và những người có nhu cầu **nâng cao kiến thức** trong lĩnh vực này.

Mục tiêu của chiến dịch cũng là **gia tăng lượng truy cập** và tạo dựng **lòng tin** và **sự gắn kết** từ phía khách hàng.

# 2. QUÁ TRÌNH XÁC ĐỊNH CÁC CHỈ SỐ PHÂN TÍCH

## 2.1. Identify - Xác định các câu hỏi cần trả lời

### 2.1.1. Làm sạch dữ liệu bằng Python.

Một số cột chứa dữ liệu hỗn hợp, cần đưa vào cột đúng, tách thời gian từ cột 'Date', tách tên web từ 'MA Referrer' để lấy nguồn theo dõi, xử lý dữ liệu email để phân loại nhóm người dùng và lấy các cột cần thiết để báo cáo.

Ví dụ: Tách thời gian từ cột 'Date' 20/08/2021, 3:12:00 PM => 3.

Ví dụ: Tách tên web từ 'MA Referrer' https://www.google.com/ => google.

Ví dụ: Tách tên miền email từ 'MA Referrer' [abc@st.uel.com.vn](mailto:abc@st.uel.com.vn) => st.uel.com => sinh viên => "Trường Đại học Kinh tế - Luật".

**Dữ liệu gốc:**

| TÊN CỘT | KIỂU DỮ LIỆU |
| --- | --- |
| Email | object |
| Date | object |
| Type | object |
| ma_path | object |
| URL | object |
| Link | object |
| Tag | object |
| Keyword | object |
| MA URL | object |
| MA
  Referrer | object |
| IP Address | object |

**Dữ liệu sau khi được xử lý bằng Python:**

| TÊN CỘT | KIỂU DỮ LIỆU |
| --- | --- |
| Email | object |
| Date | datetime |
| Hour | time |
| Type | object |
| Tag | object |
| Keyword | object |
| Source | object |
| IP Address | object |
| Domain | object |
| Customer
  Type | object |
| University | object |

### **2.1.2. Định nghĩa dữ liệu được sử dụng để phân tích:**

| TÊN CỘT | ĐỊNH NGHĨA |
| --- | --- |
| **Email** | Email (tài khoản) của người dùng |
| **Date** | Ngày truy cập |
| **Hour** | Khung thời gian truy cập của người dùng |
| **Type** | Bấm vào bất kỳ nội dung nào |
| **Tag** | Nội dung và hành động được gắn thẻ |
| **Key Work** | Từ khóa đã tìm kiếm |
| **Source** | Theo dõi trang web người dùng truy cập |
| **IP Address** | Địa chỉ IP của khách truy cập |

## 2.2. Xây dựng chỉ số

Trong báo cáo này, 4 chỉ số sẽ được sử dụng để đánh giá hiệu quả của chiến dịch SEO:

| CHỈ SỐ | ĐỊNH NGHĨA |
| --- | --- |
| Tổng lượt xem trang | Lưu lượng xem trang |
| Trang được lập chỉ mục | Số lượng trang được lập chỉ mục bởi công cụ tìm kiếm |
| Tỷ lệ thoát | Tỷ lệ thoát (người dùng chỉ truy cập một lần và không thực hiện hành động tiếp theo) |
| Tỷ lệ thêm vào giỏ hàng | Tỷ lệ thêm vào giỏ hàng (chuyển đổi từ lượt xem trang sang hành động giỏ hàng) |

# 3. PHÂN TÍCH TÌNH HÌNH CHIẾN DỊCH TIẾP THỊ SEO CỦA CÔNG TY UNIACE

## 3.1. Tổng quan về hoạt động của website [Unicae.vn](http://unicae.vn/)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/cc4fb10a-c889-4380-9844-d6d9cdb203ba/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/04965044-80eb-4b66-96f7-eb3eadd746bf/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/8bfec364-e135-4b2b-862c-0bc9d52f94d7/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/28d57116-6230-4d1b-bf97-043b4f4af8b5/image.png)

### **3.1.1. Hiệu suất chung**

- **Lượt truy cập:** Trong tổng số **14.96k** người dùng truy cập vào website Unicae.vn, chỉ có **2,439** người đăng ký tài khoản, đạt tỷ lệ **16.31%**.
- **Add to Cart Rate (Tỷ lệ thêm vào giỏ hàng):** Đây là tỷ lệ khách hàng thêm một sản phẩm vào giỏ so với tổng số lượt truy cập. Tỷ lệ này đạt mức **4.28%**, cho thấy tỷ lệ chuyển đổi khá thấp, điều này có thể phản ánh mức độ quan tâm đến sản phẩm chưa cao.

### **3.1.2. Phân tích hành vi người dùng**

- **Loại nội dung người dùng click nhiều nhất:**
    - Trang chủ là điểm dừng chính với **88.23%** tổng số lượt truy cập.
    - Các mục được quan tâm nhiều bao gồm: đăng ký tài khoản, giới thiệu về Unicae, và đặc biệt là chương trình **Young Talent Program**.
    - Điều này chỉ ra rằng đa số người dùng chỉ dừng lại ở việc tìm hiểu thông tin cơ bản về nền tảng và chưa thực hiện các hành động cụ thể khác như mua khóa học hay tham gia vào các tính năng khác của trang web.
- **Hành vi không đăng ký email:**
    - **100%** người không đăng ký mail chỉ thao tác trên trang chủ và không thực hiện thêm các hành động khác như tìm kiếm khóa học hay mua sắm.
    - Có thể thấy, trang web vẫn chưa đủ sức thuyết phục để giữ chân người dùng và khuyến khích họ khám phá thêm.

### **3.1.3. Thời điểm truy cập cao nhất**

- **Ngày 16/08** là ngày có lượng truy cập cao nhất với **4k** lượt truy cập. Lưu lượng truy cập trong các ngày khác dao động từ **2k – 4k**.
- Đặc biệt, **ngày 14/08** chứng kiến tỷ lệ thêm vào giỏ hàng (**Add to Cart Rate**) lên tới **66.14%**, cao hơn hẳn so với các ngày khác, chỉ đạt từ **1% đến 2%**. Điều này cho thấy có khả năng trang web đang chạy chương trình khuyến mãi hoặc giảm giá khóa học đặc biệt vào ngày này, dẫn đến tỷ lệ tương tác mua hàng cao hơn đáng kể.

### **3.1.4. Khung giờ cao điểm**

- Các khung giờ có lượng truy cập nhiều nhất là:
    - **9h-11h**: Khung giờ học tập và làm việc buổi sáng.
    - **14h-16h**: Khung giờ học tập và làm việc buổi chiều.
    - **20h-22h**: Khung giờ thư giãn buổi tối, nhiều người có xu hướng truy cập mạng xã hội hoặc tham gia các khóa học sau giờ làm việc.

=> Đề xuất: Website có thể tận dụng các khung giờ này để chạy quảng cáo hoặc tổ chức sự kiện, nhằm tối ưu hóa lượng tiếp cận và tương tác từ người dùng.

## **3.2. Phân tích theo nguồn lưu lượng truy cập**

### **3.2.1. Công cụ tìm kiếm**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/07767927-6fda-42fb-b20c-0a2dfe017a0d/image.png)

- **52.02%** người dùng truy cập trực tiếp vào website, cho thấy những người này có thể đã biết đến Unicae từ trước, thông qua các hoạt động quảng bá hoặc đã từng tham gia các khóa học.
- **15.57k** lượt truy cập sử dụng **Google** để tìm kiếm website, các nguồn khác bao gồm **Facebook**, **Coccoc**, và một số công cụ tìm kiếm khác.

### **3.2.2. Thời gian truy cập từ các nguồn**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/95016e9f-37e5-414c-958f-4a4e1684956b/image.png)

- Người dùng truy cập trực tiếp chủ yếu vào lúc **12h** trưa, trong khi người dùng đến từ Google và các công cụ khác truy cập nhiều nhất trong khung giờ từ **9h-11h** và **14h-16h**, trùng với giờ làm việc.

## **3.3. Phân tích người dùng**

### **3.3.1. Tỷ lệ đăng ký tài khoản**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/31eeccfb-761d-43d2-8640-6abeae57d975/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/db278c0a-0427-45f3-9c37-b6d982acae89/image.png)

- **59.97%** người dùng truy cập mà không đăng ký tài khoản, đây là một tỷ lệ phổ biến, vì không phải ai cũng có nhu cầu đăng ký để mua sản phẩm hoặc tương tác sâu hơn trên website.
- Trong số những người dùng đăng ký tài khoản:
    - **35.35%** sử dụng email có đuôi **@gmail.com** (Normal), đây là nhóm người dùng phổ biến nhất.
    - **2.68%** sử dụng email sinh viên có đuôi **.edu** (Student), cho thấy mức độ tham gia của sinh viên còn hạn chế.
    - **2%** sử dụng email của doanh nghiệp như **@outlook.com** (Work).

### **3.3.2. Phân bố theo các trường đại học**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/6a5a3c7c-c3f6-4853-a778-8214d86d1dfc/image.png)

- Hai trường có nhiều lượt truy cập nhất là:
    - **UEF** (Đại học Kinh tế - Tài chính TP.HCM)
    - **UEH** (Đại học Kinh tế TP.HCM)
- Trong nhóm các trường top đầu, chỉ có **FTU** (Đại học Ngoại thương) nằm tại Hà Nội, tuy nhiên, lượng truy cập từ sinh viên trường này cũng không nhiều.

### **3.3.3. Thói quen truy cập**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/68d2451f-bb37-40fa-9e6b-4d1536c4c26f/image.png)

- Người dùng không đăng ký tài khoản thường truy cập nhiều nhất trong các khung giờ từ **9h-11h**, **14h-16h** và đặc biệt vào khung giờ nghỉ ngơi **22h-23h**.
- **12h** trưa là thời điểm mà cả người dùng Normal, Student và Work truy cập nhiều nhất. Đây có thể là thời gian nghỉ trưa của họ, và họ thường tranh thủ lướt web hoặc tìm kiếm thông tin trong khoảng thời gian này.

### **3.3.4. Phân tích hành vi tìm kiếm và loại nội dung**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f0b482dd-ba81-4e7b-9b52-d1f61affe890/ebb4cbe5-2d52-43dc-803f-95bea9cbda12/image.png)

- Người dùng không đăng ký thường sử dụng **Google** để tìm kiếm trang web nhiều hơn các nhóm khác. Trong khi đó, người dùng đã đăng ký có xu hướng vào web trực tiếp mà không cần tìm kiếm qua công cụ thứ ba.
- **Nội dung kỹ năng** (Skill-based content) được người dùng Work và Normal truy cập nhiều nhất với tỷ lệ **xấp xỉ 90%**, trong khi **43.06%** người dùng không đăng ký lại quan tâm đến các nội dung liên quan đến **Dữ liệu** (Data-related content), bao gồm các chủ đề như Excel, SQL, Power BI,…

# **4. Kết luận và đề xuất**

- **Tối ưu hóa trang chủ:**
    - Trang chủ có tỷ lệ thoát cao, cho thấy giao diện và nội dung hiện tại chưa đủ sức thuyết phục người dùng khám phá thêm. Cần cải tiến giao diện người dùng (UI) và nội dung để thu hút người dùng tương tác nhiều hơn, chẳng hạn như gợi ý khóa học, lời kêu gọi hành động (CTA) mạnh mẽ hơn.
- **Chạy quảng cáo và khuyến mãi trong các khung giờ cao điểm:**
    - Nên triển khai các chiến dịch quảng cáo vào các khung giờ truy cập cao như **9h-11h**, **14h-16h**, và **20h-22h**, đồng thời tận dụng thêm **12h** trưa là thời điểm mà cả người dùng sinh viên và dân văn phòng thường truy cập.
- **Tập trung vào nội dung kỹ năng và dữ liệu:**
    - Người dùng Work và Normal quan tâm rất nhiều đến nội dung kỹ năng, trong khi nhóm không đăng ký lại chú trọng vào dữ liệu. Điều này có thể định hướng cho việc phát triển các khóa học và chương trình quảng bá phù hợp cho từng nhóm đối tượng.
- **Tăng cường các chương trình khuyến mãi:**
    - Ngày 14/08 có tỷ lệ Add to Cart đột biến nhờ vào khả năng có các chương trình khuyến mãi, do đó, việc triển khai các chương trình ưu đãi định kỳ có thể giúp tăng doanh thu và tỷ lệ chuyển đổi.

# 5. Tổng kết

  Dự án phân tích hoạt động website **Unicae.vn** đã cung cấp cái nhìn chi tiết về hiệu suất tổng thể và hành vi người dùng. Với **14.96k** lượt truy cập nhưng chỉ có **16.31%** đăng ký tài khoản, điều này cho thấy cơ hội tối ưu hóa cao về mặt chuyển đổi. Hầu hết người dùng tập trung vào trang chủ và ít thực hiện các tương tác khác, cho thấy cần cải thiện nội dung và giao diện để thu hút người dùng khám phá sâu hơn. Phân tích cũng chỉ ra các khung giờ cao điểm như **9h-11h**, **14h-16h**, và **20h-22h**, là thời điểm vàng cho việc chạy quảng cáo và các chương trình khuyến mãi. Người dùng dân văn phòng và sinh viên từ các trường kinh tế lớn là nhóm mục tiêu quan trọng, với nội dung kỹ năng và dữ liệu nhận được sự quan tâm cao nhất. Tỷ lệ Add to Cart tăng đột biến vào ngày có chương trình khuyến mãi gợi ý rằng các ưu đãi và sự kiện đặc biệt là cách hiệu quả để tăng tương tác và doanh thu. Dựa trên kết quả này, dự án đề xuất tập trung vào việc cải thiện giao diện trang chủ, khai thác các khung giờ cao điểm, và phát triển nội dung phù hợp với các nhóm đối tượng chính, nhằm tối ưu hóa trải nghiệm người dùng và tăng cường hiệu quả kinh doanh của website.
