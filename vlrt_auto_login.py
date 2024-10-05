import subprocess
import time
import pyautogui
import pygetwindow as gw
import os

# 1. 使用したいアカウントを選ぶ
accounts = {
    '1': {'name': '過マンガン酸カリウム', 'id': 'subakakun', 'password': '56u5uc3e'},
    '2': {'name': 'ねるねるねるね。', 'id': 'subakakun2', 'password': '56u5uc3e'},
}

print("使用したいアカウントを選んでください:")
print("0: キャンセル")
for key in accounts:
    print(f"{key}: {accounts[key]['name']}")

choice = input("番号を選択してください: ")

if choice == '0':
    print("自動ログインを中止します。")
    exit()

if choice not in accounts:
    print("無効な選択です。終了します。")
    exit()

selected_account = accounts[choice]
id = selected_account['id']
password = selected_account['password']

# 2. 自動でRiot Clientを開く
riot_client_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
subprocess.Popen(riot_client_path)

# Riot Clientの起動を待つ（Riot Clientの起動に時間がかかる場合は調整）
time.sleep(10)

# 3. ウィンドウのフォーカスを自動的に取得
windows = gw.getWindowsWithTitle("Riot Client")  # ウィンドウタイトルで検索
if len(windows) == 0:
    print("Riot Clientのウィンドウが見つかりません。")
    exit()

riot_window = windows[0]
riot_window.activate()  # ウィンドウをフォーカス

# 4. 自動でIDとパスワードが入力される
time.sleep(1)  # ウィンドウがフォーカスされるまで少し待機
pyautogui.write(id)  # IDを入力
pyautogui.press('tab')  # パスワード欄に移動
pyautogui.write(password)  # パスワードを入力

# 5. 自動でログインする
pyautogui.press('enter')  # Enterキーでログイン

print("ログインが完了しました。Valorantを起動します。")

# 6. Valorantを起動
time.sleep(10)  # ログイン処理の完了を待つ

riot_client_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
valorant_launch_args = "--launch-product=valorant --launch-patchline=live"

try:
    subprocess.Popen([riot_client_path, valorant_launch_args])
    print("Riot Clientを介してValorantを起動しました。ゲームの読み込みを待っています...")
except Exception as e:
    print(f"Valorantの起動に失敗しました。エラー: {e}")
    print("手動でValorantを起動してください。")

# 7. Valorantの起動を待つ
time.sleep(60)  # Valorantの起動を待つ（起動時間に応じて調整が必要）

# 8. Valorantウィンドウにフォーカスを移す
valorant_window = gw.getWindowsWithTitle("VALORANT")
if valorant_window:
    valorant_window[0].activate()
    print("Valorantウィンドウにフォーカスしました。")
else:
    print("Valorantウィンドウが見つかりません。手動で操作してください。")

# プレイボタンのクリックは省略しました。必要な場合は、座標を指定して実行できます。
# 例: pyautogui.click(x=960, y=540)  # 画面中央をクリック

print("Valorantが起動しました。ゲームを開始してください。")
