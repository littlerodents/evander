# 导入我们需要的工具包
import os
import shutil

# --- 你需要修改的配置 ---
# 1. 你要整理的文件夹路径 (注意：路径里的斜杠'\'可能需要写成'\\')
source_dir = "C:\\Users\\你的用户名\\Downloads" 

# 2. 各种文件类型对应的目标文件夹
#    键是文件夹名，值是该文件夹包含的文件后缀名列表
destination_dirs = {
    "文档": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "视频": [".mp4", ".mov", ".avi", ".mkv"],
    "压缩包": [".zip", ".rar", ".7z"],
    "其他": [] # 用于存放未分类的文件
}
# --- 配置结束 ---


print(f"开始整理文件夹：{source_dir}")

# 1. 检查并创建目标文件夹
for dir_name in destination_dirs.keys():
    dir_path = os.path.join(source_dir, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"创建文件夹：{dir_path}")

# 2. 遍历源文件夹中的所有文件
for filename in os.listdir(source_dir):
    source_path = os.path.join(source_dir, filename)

    # 如果是文件夹，就跳过
    if os.path.isdir(source_path):
        continue

    # 3. 判断文件类型并移动
    moved = False
    for dir_name, extensions in destination_dirs.items():
        # 检查文件名是否以指定的任一后缀名结尾
        if any(filename.lower().endswith(ext) for ext in extensions):
            destination_path = os.path.join(source_dir, dir_name, filename)
            shutil.move(source_path, destination_path)
            print(f"移动文件：{filename} -> {dir_name} 文件夹")
            moved = True
            break
    
    # 4. 如果没有找到对应的分类，移动到“其他”文件夹
    if not moved:
        other_dir_path = os.path.join(source_dir, "其他")
        destination_path = os.path.join(other_dir_path, filename)
        shutil.move(source_path, destination_path)
        print(f"移动文件：{filename} -> 其他 文件夹")


print("整理完毕！")
