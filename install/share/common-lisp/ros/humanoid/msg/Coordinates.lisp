; Auto-generated. Do not edit!


(cl:in-package humanoid-msg)


;//! \htmlinclude Coordinates.msg.html

(cl:defclass <Coordinates> (roslisp-msg-protocol:ros-message)
  ((y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0))
)

(cl:defclass Coordinates (<Coordinates>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Coordinates>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Coordinates)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name humanoid-msg:<Coordinates> is deprecated: use humanoid-msg:Coordinates instead.")))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Coordinates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader humanoid-msg:y-val is deprecated.  Use humanoid-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Coordinates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader humanoid-msg:x-val is deprecated.  Use humanoid-msg:x instead.")
  (x m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Coordinates>) ostream)
  "Serializes a message object of type '<Coordinates>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Coordinates>) istream)
  "Deserializes a message object of type '<Coordinates>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Coordinates>)))
  "Returns string type for a message object of type '<Coordinates>"
  "humanoid/Coordinates")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Coordinates)))
  "Returns string type for a message object of type 'Coordinates"
  "humanoid/Coordinates")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Coordinates>)))
  "Returns md5sum for a message object of type '<Coordinates>"
  "aedfd35910af15d9f768c14bffadd55d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Coordinates)))
  "Returns md5sum for a message object of type 'Coordinates"
  "aedfd35910af15d9f768c14bffadd55d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Coordinates>)))
  "Returns full string definition for message of type '<Coordinates>"
  (cl:format cl:nil "float64 y~%float64 x~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Coordinates)))
  "Returns full string definition for message of type 'Coordinates"
  (cl:format cl:nil "float64 y~%float64 x~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Coordinates>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Coordinates>))
  "Converts a ROS message object to a list"
  (cl:list 'Coordinates
    (cl:cons ':y (y msg))
    (cl:cons ':x (x msg))
))
