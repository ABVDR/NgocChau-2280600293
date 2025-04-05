from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Hỏi người dùng muốn thêm bao nhiêu giao dịch
print("Nhập 'x' để dừng lại khi không muốn thêm giao dịch nữa.")
while True:
    sender = input("Nhập tên người gửi: ")
    if sender.lower() == 'x':  # Kiểm tra nếu người dùng nhập 'x'
        break
    receiver = input("Nhập tên người nhận: ")
    if receiver.lower() == 'x':  # Kiểm tra nếu người dùng nhập 'x'
        break
    try:
        amount = float(input(f"Nhập số tiền chuyển từ {sender} đến {receiver}: "))
    except ValueError:
        print("Số tiền không hợp lệ, vui lòng nhập lại.")
        continue
    my_blockchain.add_transaction(sender, receiver, amount)

# Đào một block mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Thời gian:", block.timestamp)
    print("Giao dịch:", block.transactions)
    print("Proof:", block.proof)
    print("Hash của block trước:", block.previous_hash)
    print("Hash của block này:", block.hash)
    print("--------------------------------")

# Kiểm tra tính hợp lệ của blockchain
print("Blockchain có hợp lệ không:", my_blockchain.is_chain_valid(my_blockchain.chain))
