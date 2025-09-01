;; Auto-generated. Do not edit!


(when (boundp 'humanoid::Coordinates)
  (if (not (find-package "HUMANOID"))
    (make-package "HUMANOID"))
  (shadow 'Coordinates (find-package "HUMANOID")))
(unless (find-package "HUMANOID::COORDINATES")
  (make-package "HUMANOID::COORDINATES"))

(in-package "ROS")
;;//! \htmlinclude Coordinates.msg.html


(defclass humanoid::Coordinates
  :super ros::object
  :slots (_y _x ))

(defmethod humanoid::Coordinates
  (:init
   (&key
    ((:y __y) 0.0)
    ((:x __x) 0.0)
    )
   (send-super :init)
   (setq _y (float __y))
   (setq _x (float __x))
   self)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:serialization-length
   ()
   (+
    ;; float64 _y
    8
    ;; float64 _x
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get humanoid::Coordinates :md5sum-) "aedfd35910af15d9f768c14bffadd55d")
(setf (get humanoid::Coordinates :datatype-) "humanoid/Coordinates")
(setf (get humanoid::Coordinates :definition-)
      "float64 y
float64 x
")



(provide :humanoid/Coordinates "aedfd35910af15d9f768c14bffadd55d")


