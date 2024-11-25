from pathlib import Path
import matplotlib.pyplot as plt

# extra code – the next 5 lines define the default font sizes
plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

class HistogramProcess:
    """
    Lớp `HistogramProcess` thực hiện khởi tạo một thư mục và lưu các hình ảnh xử lý, hoặc biểu đồ dữ liệu vào trong thư mục của các chương!
    """
    def __init__(self, path_dir):
        self.IMAGES_PATH = Path(path_dir)
        self.IMAGES_PATH.mkdir(parents=True, exist_ok=True)
        
    def save_fig(self, fig_id, tight_layout=True, fig_extension="png", resolution=300):
        """
        Phương thức lưu biểu đồ dưới dạng tệp hình ảnh.

        Args:
        - fig_id (str): Tên tệp hình ảnh.
        - tight_layout (bool): Nếu True, tự động điều chỉnh bố cục biểu đồ.
        - fig_extension (str): Định dạng tệp hình ảnh (mặc định là 'png').
        - resolution (int): Độ phân giải của hình ảnh (DPI, mặc định là 300).
        """
        path = self.IMAGES_PATH / f"{fig_id}.{fig_extension}"
        if tight_layout:
            plt.tight_layout()
        plt.savefig(path, format=fig_extension, dpi=resolution)
        print(f"Đã lưu hình ảnh {fig_id}.{fig_extension} tại: {path.resolve()}")  # In ra đường dẫn đầy đủ

    


