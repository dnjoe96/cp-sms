from app import app, sms, db
from flask import render_template, request, flash, redirect, url_for
from app.models import Outgoing


@app.route("/", methods=["GET", "POST"])
def main():
    senderID = '23233222'
    if request.method == "POST":
        sms_message = request.form['smsMessage']
        phone_number = request.form['phoneNumber']
        sender = request.form['sender']
        # spliting the numbers in case of multiple numbers been added into the list
        num = phone_number.split(',')

        print(sms_message)
        print(num)
        try:
            response = sms.send(sms_message, num)
            print(response)

        except Exception as e:
            flash(
                'Encountered an error ({}) while sending message. Ensure that all number is correct and seperate with comma if more than one number'.format(e),
                'danger')
            return redirect(url_for('main'))
            # adding message to the database
        for number in num:
            msg = Outgoing(number, sms_message)    # sender ID will be passed in here when i obtain it
            db.session.add(msg)
            db.session.commit()
        flash("message sent successfully. {}".format(response['SMSMessageData']['Message']), "success")
        return redirect(url_for('main'))

    return render_template('index.html', senderID=senderID)


@app.route('/outgoing', methods=['GET'])
def outgoing():
    # querying the messages from the database in descending order of time sent
    msgs = Outgoing.query.order_by(Outgoing.time_sent.desc()).all()

    return render_template('message.html', msgs=msgs)


# free end point for carrying out tests
@app.route("/tray", methods=["GET", "POST"])
def tray():
    pass


# endpoint for deleting messages from the database
@app.route('/delete/<ID>', methods=['POST'])
def delete(ID):
    Outgoing.query.filter_by(id=ID).delete()
    db.session.commit()

    flash('message has been deleted', 'success')
    return redirect(url_for('outgoing'))
